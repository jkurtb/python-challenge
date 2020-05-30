#Import Modules
import os
import csv
#Set file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Set an empty list to append values
count_month = []
netGain_loss = []
changes_profit = []

#Open/read csv file and skip the headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

#Loop through rows to append the total months and net gain/loss to the list
    for row in csvreader:
        count_month.append(row[0])
        netGain_loss.append(int(row[1]))

#Loop through net gain/loss to compute the difference between two months then append to the monthly changes
    for profit in range(len(netGain_loss)-1):
        changes_profit.append(netGain_loss[profit+1]-netGain_loss[profit])

#Calculate total number of months, profit, & average change
        total_months = len(count_month)
        total_profit = sum(netGain_loss)
        average_change = round(sum(changes_profit)/len(changes_profit),2)

#Determine the greatest gain/loss in profits
        Great_increase = max(changes_profit)
        Great_decrease = min(changes_profit)

#Determine the month associated with the greatest gain/loss in profits using index, selecting the following month's value
        Month_max = changes_profit.index(max(changes_profit))+1
        Month_min = changes_profit.index(min(changes_profit))+1

#Print Analysis to Gitbash
print("Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {count_month[Month_max]} (${(str(Great_increase))})")
print(f"Greatest Decrease in Profits: {count_month[Month_min]} (${(str(Great_decrease))})")

#Export the Analysis into a text file
file_to_output = os.path.join("..","Pybank", "Output_Analysis")
with open(file_to_output, "w", newline="") as txtfile: 
        txtfile.write("Financial Analysis\n")
        txtfile.write(f"---------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${total_profit}\n")
        txtfile.write(f"Average Change: ${average_change}\n")
        txtfile.write(f"Greatest Increase in Profits: {count_month[Month_max]} (${(str(Great_increase))})\n")
        txtfile.write(f"Greatest Decrease in Profits: {count_month[Month_min]} (${(str(Great_decrease))})\n")
