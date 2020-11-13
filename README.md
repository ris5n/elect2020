# elect2020
Election Returns Analysis

You can run the .py file by changing the Rest URL for New York Times, the data will be downloaded and processed

In the /results/election_2020 - the results are tabulated
Data dictionary is as follows:
vote_share : the vote_share data retrieved from the NYT input json file
votes : incremental number of votes over timestamps
eevp : unknown
eevp_source: unknown identifier
timestamp: the actual timestamp in UTC posted
trumpd : parsed share of vote for Trump
bidenj: parsed share of vote for Biden
third_party : (1-trumpd-bidenj) - so that 100% of the votes in current timestamp are allocated
trumpd_votes : allocated share of Trump votes (trumpd * votes)
bidenj_votes : allocated share of Biden votes (bidenj * votes)
third_party_votes : allocated share of Third Party votes (third_party * votes)
trumpd_votes_diff : difference of votes for Trump in consecutive timestamps. If negative, votes were removed from Trump
bidenj_votes_diff : difference of votes for Biden in consecutive timestamps, If negative, votes were removed from Biden
third_party_votes_diff : difference of votes for TP in consecutive timestamps

abs_trumpd_votes_diff : absolute values(trumpd_votes_diff)
abs_bidenj_votes_diff : absolute values(bidenj_votes_diff)
abs_third_party_votes_diff : absolute values(third_party_votes_diff)

Increase in Votes per TS : Increase in votes from 1 timestamp to next
Delta_Trump_Biden : trumpd_votes - bidenj_votes
