# Election Audit

## Overview of Project
The purpose of this analysis was to audit the results of a congressional election, at the request of the election commission. I analyzed the votes cast during the election in relation to both candidates and counties using a Python script. First, I determined the number of votes for each candidate, the proportion of total votes that each candidate received, and the winning candidate. Second, I calculated the voter turnout for each county, the percentage of votes from each county relative to the total vote count, and the county with the highest voter turnout.

## Election Audit Results
* 369,711 votes were cast in this election

* Vote breakdown by county:
    * Denver County: 306,055 votes (82.8% of total)
    * Jefferson County: 38,855 votes (10.5% of total)
    * Arapahoe County: 24,801 votes (6.7% of total)
* Denver County had the largest turnout

* Vote breakdown by candidate:
    * Diana DeGette: 272,892 votes (73.8% of total)
    * Charles Casper Stockham: 85,213 votes (23.0% of total)
    * Raymon Anthony Doane: 11,606 votes (3.1% of total)
* Diana DeGette won the election, with 73.8% of the vote and 272,892 votes in total

## Election Audit Summary
This Python script can be modified to audit virtually any election. However, the election data must be in tabular format -- with rows corresponding to individual votes -- and there must be columns recording (a) the candidate for which the vote was cast and (b) the county from which the vote was cast. The script can be adjusted to read in a CSV file with any set of columns as long as these condtions are satisfied. On lines 47 and 50, the indices can be changed to that of the corresponding columns in a different dataset. ![Code1](https://user-images.githubusercontent.com/87445739/132418564-9a086248-acbc-4ecb-b1a2-72c4974b5ccd.png)

If the data contains variables besides candidate name and county, the script can also be modified to analyze these as well. If the election data file contained a column "political_party", one could refactor the same code used to track the number of votes per candidate. This would be a simple process: only the variable names, the reference to the column in the dataset on line 47, and the write-up into the txt file would have to be changed. The refactored code would record the names of each political party, count the number of votes per party, and calculate each party's percentage of the total vote. The political party of each candidate could also be determined by indexing through the candidate_options list and the corresponding party_options list, and the script could be modified to display this information in the txt file. 
