import os
import csv
csvpath="/Users/mouni/Documents/PREWORK_MP/Module-3/Budget_data.csv"
with open(csvpath) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_file)
    count_months=0
    tot_profit_loss=0
    diff_profit_loss=0
    total_diff=0
    for row in csv_reader:
        count_months=count_months+1
        tot_profit_loss=tot_profit_loss+int(row[1])
        if count_months==1:
            profit_loss_previous=int(row[1])
            continue
        
        diff_profit_loss=int(row[1])-profit_loss_previous
        total_diff=total_diff+diff_profit_loss
        profit_loss_previous=int(row[1])
    average_change=(total_diff/(count_months-1))
print("Total Months: "+str(count_months))
print("Total Profit/Losses: $"+str(tot_profit_loss))
print("Average change: $"+str(average_change))