import os
import csv
csv_path="/Users/mouni/Documents/GitHub/election/UTAUS201810DATA2/Python/Homework/Instructions/PyPoll/Resources/election_data.csv"
with open(csv_path) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)
    count_voters=0
    count_khan=0
    count_correy=0
    count_li=0
    count_otooley=0
    candidate_list=[]
    candidate_dict={}
    for row in csv_reader:
        count_voters=count_voters+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2]=="Khan":
            count_khan=count_khan+1
        if row[2]=="Correy":
            count_correy=count_correy+1
        if row[2]=="Li":
            count_li=count_li+1
        if row[2]=="O'Tooley":
            count_otooley=count_otooley+1
        for name,count in candidate_dict.items():
            if 
            winner=name
        khan_percentage=(count_khan/count_voters)*100
        correy_percentage=(count_correy/count_voters)*100
        li_percentage=(count_li/count_voters)*100
        otooley_percentage=(count_otooley/count_voters)*100
    print("Election results\n------------")
    print(f"Total votes: {count_voters}\n-------------") 
    print(f"Khan: {khan_percentage:.3f}% ({count_khan})")
    print(f"Correy: {correy_percentage:.3f}% ({count_correy})")
    print(f"Li: {li_percentage:.3f}% ({count_li})")
    print(f"O'Tooley: {otooley_percentage:.3f}% ({count_otooley})")
    print(f"------------\nWinner: {winner}")
       
    
    

