#The data that need to be retrieved
#1.The total number of votes cast
#2.Complete list of candidates who received the vvotes
#3.The percentage of vote each candiate vote
#4.The toatal number votes each candiate won
#5.The winner of the election based on popular vote
import csv 
import os

type_election = input("Election That needs to be analysed")

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Election_Analysis\\Resources", "election_results.csv")
file_to_save = os.path.join("Election_Analysis\\analysis", "election_results.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
# election_data is file variable
    file_reader = csv.reader(election_data, delimiter=",")
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)   

    # Initialize a total vote counter.
    total_votes = 0 
    candidate_options = []
    county_options =[]
    #Declare the empty dictionary.
    candidate_votes = {}
    county_votes={}
    candidate_vote_per = {}
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0.00
    winning_county =""
    winning_county_count =0
    winning_county_percentage =0.00
        # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        i=headers.index('Candidate')
        j=headers.index('County')
        #get the candidate name
        candidate_name = row[i]
        county_name = row[j]
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 1
        else:
           #candidate_votes[candidate_name] =candidate_votes.get(candidate_name) +1  
           candidate_votes[candidate_name] +=1   
        if county_name not in county_options:
           county_options.append(county_name)
           county_votes[county_name]=1
        else:
           #candidate_votes[candidate_name] =candidate_votes.get(candidate_name) +1  
           county_votes[county_name] +=1     
#Print the total votes.
#print(f"Total_votes:{total_votes}")
#print(candidate_options)
#print(candidate_votes)
#print(county_options)
#print(county_votes)

election_results = (
        f"\n{type_election:} Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
print(election_results, end="")

with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write(election_results)
    #print(f"County Votes:\n" )
    
    for county in county_votes :
        county_percentage =  round((county_votes[county]/total_votes)*100,2)
        county_results =(f"{county}:{county_percentage:.1f}% ({county_votes[county]:,})\n")
        print(county_results)
        txt_file.write(county_results)
        if winning_county_count < county_votes[county]:
           winning_county_count  =county_votes[county]
           winning_county = county
    winning_county_summary=(
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary) 
    for name in candidate_votes:
            vote_percentage = round((candidate_votes[name]/total_votes)*100,2)
            #print(f"{name}: received {vote_percentage:.1f}% of the vote.")
            candidate_results=(f"{name}: {vote_percentage:.1f}% ({candidate_votes[name]:,})\n")
            print(candidate_results)
            # Write some data to the file.
            txt_file.write(candidate_results) 
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
    #print(candidate_vote_per)
    txt_file.write(winning_candidate_summary)
#win_candidate = max(candidate_vote_per, key=candidate_vote_per.get)
#print(win_candidate)

 

