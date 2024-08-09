import os
import csv

#import the files: election_data.csv
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath,) as file:
    reader=csv.reader(file, delimiter=',')
    votes=list(reader)
    total_votes=len(votes) - 1

print("Election Results")
print("----------------")

print(f"Total votes: {total_votes}")
print("-------------------")

candidates={}
for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

for candidate, vote_count in candidates.items():
    percentage= round((vote_count/total_votes)*100,3)

    print(f"{candidate}:\t{percentage}%\t {vote_count}")
print("---------------------------------")


#winning_number = 0
winning_name = 0 
vote_list = []
for candidate, vote_count in candidates.items():
    vote_list.append(vote_count)

    #if vote_count > winning_number:
print(max(vote_list))
for candidate, vote_count in candidates.items():
    percentage= round((vote_count/total_votes)*100,3)
    if max(vote_list) == vote_count:
        print(f'Winner: {candidate}')









    

# Variables to track the financila chnages
#total_months = 0
#overall_total= 0.00
#net_change=[]
#increase=-999999
#decrease=999999




# Read the csv file and process it's values/records
#Jan: 2 and Feb : 18
# net_change_feb/jan = feb- Jan
# totls_mot+1
# net_change.appned(net_change_feb/jan )

#if net_chane<deacrese
   #decred= net_change
# if net_change>increase
#incrase= netchange

# avarage= net_chane/months
# average = net_chnage/len(net_change)

# Generate the putput that is going to include all the varibles. Store the values in the txt file and store in the analysis
# total number of months is total_months 
# The overaal net gain is overall_total
# The average netchane os net_change
# The greatest increase is : increase
# decrease

#function for counting rows
#def count_rows(filename)