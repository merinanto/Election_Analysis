#The data that need to be retrieved
#1.The total number of votes cast
#2.Complete list of candidates who received the vvotes
#3.The percentage of vote each candiate vote
#4.The toatal number votes each candiate won
#5.The winner of the election based on popular vote
import csv 
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

file_to_load = os.path.join("Election_Analysis\\Resources", "election_results.csv")
print(file_to_load)
file_to_save = os.path.join("Election_Analysis\\analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:
# election_data is file variable
    file_reader = csv.reader(election_data, delimiter=",")
     # To do: perform analysis.
     #print(election_data)

         # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    # Print the header row.
    headers = next(file_reader)
    print(headers)   


with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    # Read the file object with the reader function.
    #file_reader = csv.reader(election_data)    

