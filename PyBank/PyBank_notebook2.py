# initiate by importing modules

import os
import csv

csvpath = os.path.join('budget_data.csv')

# lists to store data
# month_count = []

# average(budget_data):


with open(csvpath, newline='') as csvfile:
    # csv reader specifies delimiter and variable that hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader)
    revenue = []
    date = []
    change = []

    # loop for total months
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

# follow format from instructions and print

    print("Financial Analysis")

    print("-----------------------------------")

    print("Total Months:", len(date))

    print("Total Revenue: $", sum(revenue))



    #figure out the difference from the rows and get the min and max per month
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
        avg_change = sum(change)/len(change)

        max_change = max(change)

        min_change = min(change)

        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])


    print("Avereage Revenue Change: $", round(avg_change))
    print("Greatest Increase in Revenue:", max_change_date,"($", max_change,")")
    print("Greatest Decrease in Revenue:", min_change_date,"($", min_change,")")