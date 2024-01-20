# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:20:04 2024

@author: chris
"""

import csv

# Specify the full file path using raw string notation
file_path = r"C:/Users/chris/OneDrive/Desktop/Columbia Class/Module3_challenge/PyPoll/Resources/election_data.csv"

# Create an empty list to store the data
data = []

# Open the CSV file in read mode
with open(file_path, 'r') as csvfile:
   # Create a CSV reader object
   csv_reader = csv.reader(csvfile)

   # Skip the header row 
   next(csv_reader, None) 
   

   # Read each row into the data list
   for row in csv_reader:
       data.append(row)

# Display the first few rows to verify successful reading
print(data[:5])  # Print the first 5 rows

# Store the file path as a string
election_data_file_path = "C:/Users/chris/OneDrive/Desktop/Columbia Class/Module3_challenge/PyPoll/Resources/election_data.csv"

# Define a list to store the votes
votes = []

votes = data

# Calculate the total number of votes cast
total_votes = len(votes)

# Print the total number of votes
print("Total number of votes cast:", total_votes)


# Read the CSV file and store data in a list of dictionaries
election_data_list = []
with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        election_data_list.append(row)

# Display the first few rows to verify successful reading
for i in range(min(5, len(election_data_list))):
    print(election_data_list[i])

# Calculate the total number of votes cast
total_votes = len(election_data_list)
print("Total number of votes cast:", total_votes)

# Provide a complete list of candidates who received votes
candidates = set(row["Candidate"] for row in election_data_list)
print("Candidates:", candidates)

# Count the number of votes for each candidate
candidate_votes = {candidate: sum(1 for row in election_data_list if row["Candidate"] == candidate) for candidate in candidates}
print("Votes per candidate:", candidate_votes)

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
print("Percentage of votes per candidate:", percentages)

# Find the winner
winner = max(percentages, key=percentages.get)
print("Winner:", winner, "with", candidate_votes[winner], "votes!")

# Save results to a text file
output_path = r"C:/Users/chris/OneDrive/Desktop/Columbia Class/Module3_challenge/PyPoll/Resources/election_data.txt"
with open(output_path, 'w') as text_file:
    text_file.write("Election Data:\n")
    text_file.write("- Total number of votes cast: {}\n".format(total_votes))
    text_file.write("- Candidates: {}\n".format(candidates))
    text_file.write("- Votes per candidate: {}\n".format(candidate_votes))
    text_file.write("- Percentage of votes per candidate: {}\n".format(percentages))
    text_file.write("- Winner: {} with {} votes!\n".format(winner, candidate_votes[winner]))



