# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:48:44 2024

@author: chris
"""

import csv

# Specify the full file path using raw string notation
file_path = r"C:/Users/chris/OneDrive/Desktop/Columbia Class/Module3_challenge/PyBank/Resources/budget_data.csv"

# Create an empty list to store the data
data = []

# Open the CSV file in read mode
with open(file_path, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row (if present)
    next(csvreader)  # Skip the first row (header)

    # Read each row into the data list
    for row in csvreader:
        data.append(row)

# Access and process the data as needed
print(data)  # Example: Print the raw data list

import os

# Store filepath in a variable using os.path.join
budget_data = os.path.join("C:/Users/chris/OneDrive/Desktop/Columbia Class/Module3_challenge/PyBank/Resources", "budget_data.csv")

# Read the CSV data into a list
data = []
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        data.append(row)

# Get the total number of months (assuming each row represents a month)
total_months = len(data)

# Print the result
print("Total number of months:", total_months)

# Initialize a variable to store the net total
net_total = 0

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

 # Iterate through each row and calculate the net total
    for row in csvreader:
        profit_loss = int(row[1]) 
        net_total += profit_loss

# Print the result
print("Net total Profit/Losses:", net_total)

# Read the CSV data into a list
data = []
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  
    for row in csvreader:
        data.append(row)

# Calculate changes (differences between consecutive values)
changes = []
for i in range(1, len(data)):
    current_profit = int(data[i][1]) 
    previous_profit = int(data[i - 1][1])
    change = current_profit - previous_profit
    changes.append(change)

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the result
print("Average change Profit/Losses:", average_change)

# Initialize variables to track maximum increase
max_increase = float('-inf')  # Negative infinity to ensure any positive increase is captured
max_increase_date = None

# Iterate through profit/loss values
for i, row in enumerate(data):
    profit = int(row[1])  # Assuming "Profit/Losses" is in the second column

    # Check if current profit is a new maximum increase
    if i > 0 and profit - int(data[i-1][1]) > max_increase:
        max_increase = profit - int(data[i-1][1])
        max_increase_date = row[0]  # Store the date (assuming it's in the first column)

# Check if any increase was found
if max_increase_date is None:
    print("No increase in profits found.")
else:
    # Display the results
    print("Date of greatest increase:", max_increase_date)
    print("Amount of greatest increase:", max_increase)
    
    # Initialize variables to track maximum decrease
max_decrease = float('inf')  # Positive infinity to ensure any negative decrease is captured
max_decrease_date = None

# Iterate through profit/loss values
for i, row in enumerate(data):
    profit = int(row[1])  # Assuming "Profit/Losses" is in the second column

    # Check if current profit is a new maximum decrease
    if i > 0 and profit - int(data[i-1][1]) < max_decrease:
        max_decrease = profit - int(data[i-1][1])
        max_decrease_date = row[0]  # Store the date (assuming it's in the first column)

# Check if any decrease was found
if max_decrease_date is None:
    print("No decrease in profits found.")
else:
    # Display the results
    print("Date of greatest decrease:", max_decrease_date)
    print("Amount of greatest decrease:", max_decrease)
    
output_file = r"C:\Users\chris\OneDrive\Desktop\Columbia Class\Module3_challenge\PyBank\Analysis\results.txt"
    
# Write the results to the output file
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("--------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Net Total: ${net_total}\n")
    output.write(f"Average Change: ${average_change:.2f}\n")
    output.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

print("Results exported to results.txt successfully!")