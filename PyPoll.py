#The data that need to be retrieved
#1.The total number of votes cast
#2.Complete list of candidates who received the vvotes
#3.The percentage of vote each candiate vote
#4.The toatal number votes each candiate won
#5.The winner of the election based on popular vote
import csv 
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Election_Analysis\\Resources", "election_results.csv")
file_to_save = os.path.join("Election_Analysis\\analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:
# election_data is file variable
    file_reader = csv.reader(election_data, delimiter=",")
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)   

    #  Initialize a total vote counter.
    total_votes = 0 
    candidate_options = []
    # Declare the empty dictionary.
    candidate_votes = {}
    candidate_vote_per = {}
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0.00
        # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        #get the candidate name
        candidate_name = row[2]
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 1
        else:
           #candidate_votes[candidate_name] =candidate_votes.get(candidate_name) +1  
           candidate_votes[candidate_name] +=1   
# 3. Print the total votes.
print(f"Total_votes:{total_votes}")
print(candidate_options)
print(candidate_votes)

for name in candidate_votes:
            vote_percentage = round((candidate_votes[name]/total_votes)*100,2)
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            print(f"{name}: {vote_percentage:.1f}% ({candidate_votes[name]:,})\n")
            if winning_count < candidate_votes[name]:
                winning_count =candidate_votes[name]
                winning_percentage = vote_percentage
                winning_candidate =name
            #candidate_votes[name].append(percentage)
            #candidate_votes.setdefault(name,percentage)
            candidate_vote_per[name] =[candidate_votes[name],vote_percentage]
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)            
print(candidate_vote_per)
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Hello World")
win_candidate = max(candidate_vote_per, key=candidate_vote_per.get)
print(win_candidate)

 

