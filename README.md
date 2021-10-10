# Election_Analysis

## Overview

The reason for this analysis was to assist with an election audit for the Colorado Board of Elections in determining the number of votes casted in total, provide a complete list of candidates that were voted for, tally the total number of votes each candidate received and the respective percent of the total votes casted and, finally, to determine the winner of the election based on popular vote.

The deliverables are broken down as follows:
  1. Provide the total number of votes casted.
  2. Provide a complete list of candidates with votes.
  3. Provide the total number of votes for each candidate.
  4. Provide the percentage of votes each candidate received.
  5. Provide the winner of the election based on popular vote.

## Resources

### Data: 
election_results.csv

### Software:
Python 3.7.6
Visual Studio Code 1.61.0

## Election-Audit Results

* How many votes were cast in this congressional election?

There was a total of 369,711 votes casted.

![total_votes_casted](https://user-images.githubusercontent.com/90632470/136713276-ae38aa9b-cdbc-447b-be76-385228927957.PNG)

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

There were 38,855 votes casted for Jefferson County.  There were 306,055 votes casted for Denver.  There were 24,801 votes casted for Arapahoe.

![total_votes_casted_by_county](https://user-images.githubusercontent.com/90632470/136713292-e73c2e5a-6e09-4d52-b5be-25838fd1ef89.PNG)

* Which county had the largest number of votes?

Denver had the largest turn out of voters by a landslide.  306,055 of the total 369,711 votes came from the county of Denver.

![largest_county_turnout](https://user-images.githubusercontent.com/90632470/136713297-80102e6d-4bc1-4a0e-a2c0-0b4c6c52cbbd.PNG)

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Charles Casper Stockham received 85,213 votes which was 23.0% of the total votes casted.  Diane DeGette received 272,892 votes which was 73.8% of the votes casted.  Raymon Anthony Doane received 11,606 votes which was 3.1% of the votes casted.

![candidates_and_totals_percentages](https://user-images.githubusercontent.com/90632470/136713302-91eeb4c6-7ea6-49b1-96f9-952d924f49d5.PNG)

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

It was also a landslide for who won the election by popular vote.  Diana DeGette won the election with 272,892 of the total 369,711 votes which was 73.8% of the total.

![winner_by_popular_vote](https://user-images.githubusercontent.com/90632470/136713305-ccf40cd6-ebf3-487e-9c6b-5878d7b03494.PNG)

## Summary

This challenge required the installation and use of Python and Visual Studio (VS) Code.  It was also requested to add, commit and push analysis results throughout the challenge via GitBash to GitHub. Mathematical equations were used to extract further information from the data file; Election Results. Upon determining who the candidates were, how many votes they each received (along with the respective percentages of the total votes each candidate received and, ultimately, the winner by popular vote the results were written to a .txt file to pass along with the final results.

I found Python to be easier to use than the prior VBA in Excel as it seems more intuitive.  Utilizing VS Code was extremely helpful to find errors quickly and the automatic color coding was quite handy as well.  I did find it tricky to ensure that my tabs are lined up properly, while VS Code makes it clear where the code is aligned on the left margin, I still needed to make sure I had it aligned properly or errors would result.  Additionally, I find that when troublesjooting, I can find myself in a bit of a mess and need to start my file over.  Not always are you able to use the Undo button and when you begin editing its easy to forget what you've edited.

### Recommendations:

The provided script was used to tally the number of candidates and counties participating in an election and the totals and percentages of each.  From the calculations, the winner by popular vote and the county with the largest voter turnout was provided.

This script can be modified to load an Excel file instead of a CSV file. In order to do this, an edit would be made to Lines 9 and 36.

    file_to_load = os.path.join("Resources", "election_results.csv")
    reader = csv.reader(election_data)

Instead of noting .csv, the script could be modified to show .xlsx instead.  This is dependent upon the file the originating data is maintained in.

If it is prefered to determine who the candidate was with the fewest votes, slight modifications could also be made for this as well.  Instead of noting a symbol of > (greater than) on line 138:

    if (votes > winning_count) and (vote_percentage > winning_percentage):

that could be reversed to a symbol of < (less than).  There are two places this edit would need to be made on this line to calculate both the fewest votes and the lowest percentage.
