#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# number of months
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    months = len(list(csvreader))
    print(months)

#total of all profits and losses
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    total = 0
    for row in csvreader:  
        total = total+int(row[1])
    print(total)


#making a list of changes and then taking the average of the list
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    last = 0
    change = 0
    totalchange = []
    for row in csvreader:
        change = int(row[1]) - last
        totalchange.append(change)
        last = int(row[1])
#the first row is included in the list and it shouldn't be, so let's just take it out
    average = ((sum(totalchange)-867884) / (len(totalchange)-1))
    average = round(average, 2)
    print(average)

#greatest increase in profits
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    last = 0
    change = 0
    totalchange = []
    for row in csvreader:
        change = int(row[1]) - last
        totalchange.append(change)
        last = int(row[1])
    totalchange.sort()
    greatest = totalchange[-1]
    print(totalchange[-1])

#greatest decrease in profits
    totalchange.sort(reverse=True)
    print(totalchange[-1])

    file = open("analysis.txt", "w") 
    file.write(f"Financial Analysis: \nTotal Months: {months}\nTotal: {total}\nAvg Change: {average}\nGreatest +: {greatest}\nGreatest -: {totalchange[-1]}")
    file.close() 






