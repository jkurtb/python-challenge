#Import modules
import os
import csv
#Set a relative file path
csvpath = os.path.join("Resources", "election_data.csv")

#Define initial counter & empty dictionaries
total_votes = 0
candidate_info = {}
percent_vote = {}
winner = None
winner_vote = 0


#Open/read csv & skip headers
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)

#Loop through rows to get the sum of all votes
    #then add items in the dictionary 
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidate_info.keys():
            candidate_info[row[2]] += 1
        else:
            candidate_info[row[2]] = 1
#Calculate each candidate's percentage vote with 3 decimal places
    for key, value in candidate_info.items():
        percent_vote[key] = "{:.3f}".format((value/total_votes)*100)

#Determine the winner based on highest votes
    for key in candidate_info.keys():
        if candidate_info[key] > winner_vote:
            winner = key
            winner_vote = candidate_info[key]

#Print analysis/results to GitBash
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for key, value in candidate_info.items():
    print(f"{key}: {percent_vote[key]}% ({value})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


