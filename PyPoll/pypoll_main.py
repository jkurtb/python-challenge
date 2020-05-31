#Import modules
import os
import csv
#Set the file path
csvpath = os.path.join("Resources", "election_data.csv")

#Define initial counter & empty dictionary
total_votes = 0
candidate_info = {}

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
    

    #check results of dictionary
    print(candidate_info.items())
    print(total_votes)


