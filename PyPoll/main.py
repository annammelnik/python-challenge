#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#total number of votes
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    votes = len(list(csvreader))
    #print(votes)

with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    list = []
    khanlist = []
    correylist = []
    lilist = []
    toollist = []
    for row in csvreader:
        if row[2] not in list:
            list.append(row[2])
    with open(csvpath, encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            if row[2] == list[0]:
                khanlist.append(row[2])
    print("Election Results:")
    print("Total Votes:")
    print(votes)
    print("Khan total votes and percentage:")
    print(len(khanlist))
    print(len(khanlist)/votes)

    with open(csvpath, encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            if row[2] == list[1]:
                correylist.append(row[2])
    print("Correy total votes and percentage:")
    print(len(correylist))
    print(len(correylist)/votes)

    with open(csvpath, encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            if row[2] == list[2]:
                lilist.append(row[2])
    print("Li total votes and percentage:")
    print(len(lilist))
    print(len(lilist)/votes)

    with open(csvpath, encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            if row[2] == list[3]:
                toollist.append(row[2])
    print("O'Tooley total votes and percentage:")
    print(len(toollist))
    print(len(toollist)/votes)
    print("Winner: ")
    print(list[0])

    file = open("analysis.txt", "w") 
    file.write(f"Election Results: \nTotal Votes: {votes}\nKhan total votes and %: {len(khanlist)}, {len(khanlist)/votes}\nCorrey total votes and %: {len(correylist)}, {len(correylist)/votes}\nLi total votes and %: {len(lilist)}, {len(lilist)/votes}\nO'Tooley total votes and %: {len(toollist)}, {len(toollist)/votes}\nWinner: {list[0]}")
    file.close() 