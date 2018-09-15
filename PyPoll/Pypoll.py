# initiate by importing modules

import os
import csv
import collections

csvpath = os.path.join("..", 'election_data.csv')

# lists to store data
# month_count = []

# average(budget_data):


with open(csvpath, newline='') as csvfile:
    # csv reader specifies delimiter and variable that hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    next(csvreader)

    total_votes = []
    Khan = 0
    Correy = 0
    Li = 0
    #O'Tooley = []
    #names = collections.Counter()
    # loop for total votes
    for row in csvreader:
        names = collections.Counter()
        total_votes.append(row[1])

        total_votes = sum(1 for row in csvreader)
        #names = [row[2]]
        #if names[2] =='Khan':
            #Khan += 1

        names[row[2]] += 1

        #Khan.append(row[2])

        #names = ["Khan", "Correy", "Li", "O'Tooley"]

        print('Election Results')

        print('-----------------')

        print("Total Votes:", (total_votes))

        print('-----------------')

        #print(Khan)

        print(names['Khan'])
        print(names['Correy'])
        print(names['Li'])
        print(names["O'tooley"])
        print('---------------')
        print('Winner is', names.most_common())
#with open("output.txt", "w") as text_file:
   # print(f"Pypoll: {}", file=text_file)