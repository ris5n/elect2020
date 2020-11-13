import pandas as pd
from glom import glom
from pandas.io.json import json_normalize
import numpy as np
import urllib3
from urllib3 import request

remote = True
input_file = '.\data\election_2020\pa_president.json'
output_file = '.\\results\election_2020\pa_president_computed.csv'
rest_url = 'https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/race-page/pennsylvania/president.json'

if remote:
    http = urllib3.PoolManager()
    res = http.request('GET', rest_url)
    elect_df_from_rest = pd.read_json(res.data)
    elect_df = pd.DataFrame(glom(elect_df_from_rest, 'data.races.0.timeseries'))
else:
    elect_df_from_csv = pd.read_json(input_file)
    elect_df = pd.DataFrame(glom(elect_df_from_csv, 'data.races.0.timeseries'))
elect_df = elect_df.join(json_normalize(elect_df.vote_shares))

#add the third party share of votes with formula (1 - (trumpd + bidenj))
elect_df['third_party'] = 1 - elect_df['trumpd'] - elect_df['bidenj']
elect_df.loc[0, 'third_party'] = 0.0

#compute the votes at each timestamp
elect_df['trumpd_votes'] = (elect_df['votes']*elect_df['trumpd']).apply(np.ceil)
elect_df['bidenj_votes'] = (elect_df['votes']*elect_df['bidenj']).apply(np.ceil)
elect_df['third_party_votes'] = (elect_df['votes']*elect_df['third_party']).apply(np.ceil)

#compute the increase in votes in consecutive timestamps
elect_df['trumpd_votes_diff'] = elect_df['trumpd_votes'].diff()
elect_df['bidenj_votes_diff'] = elect_df['bidenj_votes'].diff()
elect_df['third_party_votes_diff'] = elect_df['third_party_votes'].diff()

elect_df['abs_trumpd_votes_diff'] = elect_df['trumpd_votes'].diff().abs()
elect_df['abs_bidenj_votes_diff'] = elect_df['bidenj_votes'].diff().abs()
elect_df['abs_third_party_votes_diff'] = elect_df['third_party_votes'].diff().abs()

#compute Increase in Votes per TS
elect_df['Increase in Votes per TS'] = elect_df['votes']
elect_df['Delta_Trump_Biden'] = elect_df['trumpd_votes'] - elect_df['bidenj_votes']
print(elect_df)
elect_df.to_csv(output_file)
