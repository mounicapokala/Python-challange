import os
import csv

csvpath="/Users/mouni/Documents/GitHub/Python-challange/PyBank/Budget_data.csv"
with open(csvpath) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_file)
    count_months=0
    tot_profit_loss=0
    diff_profit_loss=0
    total_diff=0
    diff_list=[]
    max_diff=0
    min_diff=0
    diff_dict={}
    for row in csv_reader:
        count_months=count_months+1
        tot_profit_loss=tot_profit_loss+int(row[1])
        if count_months==1:
            profit_loss_previous=int(row[1])
            continue
        
        diff_profit_loss=int(row[1])-profit_loss_previous
        #greater value
        diff_list.append(diff_profit_loss)
        total_diff=total_diff+diff_profit_loss
        profit_loss_previous=int(row[1])
        diff_dict[row[0]]=diff_profit_loss
    max_diff=max(diff_list)
    min_diff=min(diff_list)
    for month,diff in diff_dict.items():
        if diff==int(max_diff):
            great_diff_month=month
        if diff==int(min_diff):
            least_diff_month=month
    average_change=(total_diff/(count_months-1))

print("Total Months: "+str(count_months))
print("Total Profit/Losses: $"+str(tot_profit_loss))
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: {great_diff_month} (${max_diff})")
print(f"Greatest decrease in profits: {least_diff_month} (${min_diff})")