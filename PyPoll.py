#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. The winner of the election based on popular vote

#Import the datetime class from the datetime module.
import datetime as dt
#Use the (now) attribute on the datetime class to get present time.
now = dt.datetime.now()
#Print the present time.
print("The time right now is", now)

#Add dependencies.
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Set total votes to 0.
total_votes = 0
#Candidate options
candidate_options = []
#Set empty candidate dictionary.
candidate_votes = {}

#Set winner variable, counts and percentage.
winner = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read file object with reader function.
    file_reader = csv.reader(election_data)

    #Read header row.
    header = next(file_reader)

    #Print each row of data:
    for row in file_reader:
        #Add to total votes.
        total_votes += 1
        #Print candidate name from each row.
        candidate_name = row[2]
        #If name doesn't match existing name..
        if candidate_name not in candidate_options:
            #Add candidate name to options.
            candidate_options.append(candidate_name)
            #Set candidate votes to 0 to begin counting.
            candidate_votes[candidate_name] = 0
        #Add votes to each candidate.
        candidate_votes[candidate_name] += 1

#Print total votes.
print(candidate_votes)

#Get votes for each candidate.
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
   
    #Determine winner.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winner = candidate_name

#Summary of results.
winning_summary = (f"-----------------------\n"
f"Winner: {winner}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-----------------------\n")
print(winning_summary)

#Close the file.
election_data.close()