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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read file object with reader function.
    file_reader = csv.reader(election_data)

    #Print each row of data:
    for row in file_reader:
        print(row)

#Print the file object.
    print(election_data)

#Close the file.
election_data.close()

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and write to the file.
with open(file_to_save,"w") as txt_file:

    #Add a header to the file.
    txt_file.write("Counties in the Election\n")

    #Add a separator line.
    txt_file.write("_________________________\n")

    #Write three counties to file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Close the file.
txt_file.close()