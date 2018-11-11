import os
import csv
import operator
csv_path="/Users/mouni/Documents/GitHub/election/UTAUS201810DATA2/Python/Homework/Instructions/PyPoll/Resources/election_data.csv"
output_path="/Users/mouni/Documents/GitHub/Python-challange/PyPoll/PyPoll.txt"
with open(csv_path) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)
    count_voters=0
    count=0
    candidate_list=[]
    all_cand_list=[]
    candidate_dict={}
    candidate_percent={}

    for row in csv_reader:
        count_voters=count_voters+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        all_cand_list.append(row[2])
       
with open(output_path,'a') as out:
    out.write("Election results\n------------\n")
    out.write(f"Total votes: {count_voters}\n-------------\n")
    print("Election results\n------------")
    print(f"Total votes: {count_voters}\n-------------") 

    for candidate in candidate_list:
        for vote_cand in all_cand_list:
            if candidate==vote_cand:
                count=count+1
        candidate_dict[candidate]=count
        count=0

    for key,values in candidate_dict.items():
        percent_vote=round((values/count_voters)*100,0)
        candidate_percent[key]=percent_vote
        print("%s: %.3f%% (%s)" %(key,percent_vote,values))
        out.write("%s: %.3f%% (%s)\n" %(key,percent_vote,values))
    winner=max(candidate_percent.items(), key=operator.itemgetter(1))[0]
    print(f"----------\nWinner: {winner}\n-----------")
    out.write(f"----------\nWinner: {winner}\n-----------")

