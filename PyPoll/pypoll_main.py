#Import modules
import os
import csv
#Set the file path
csvpath = os.path.join("Resources", "election_data.csv")

#Define initial counter & empty dictionary
total_votes = 0
candidate_info = {}
percent_vote = {}


#Open/read csv & skip headers
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)

#Loop through rows to add items in the dictionary
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidate_info.keys():
            candidate_info[row[2]] += 1
        else:
            candidate_info[row[2]] = 1

    for key, value in candidate_info.items():
        percent_vote[key] = round((value/total_votes)*100,3)



#Print analysis & results 
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for key, value in candidate_info.items():
    print(f"{key}: {percent_vote[key]}% ({value})")


