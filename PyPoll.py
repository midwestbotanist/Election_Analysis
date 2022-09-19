# The data we need to retrieve
# 1. The total number of votes to cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

        # Print the file object
        print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

        # Write three counties to the file.
        txt_file.write("Counties in the Election\n")
        txt_file.write("------------------------\n")
        txt_file.write("Arapahoen\n")
        txt_file.write("Denver\n")
        txt_file.write("Jefferson\n")


# 1. Initialize a total vote counter
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

        # Read the file object with the reader function.
        file_reader = csv.reader(election_data)

        # Print each row in the CSV file.
        headers = next(file_reader)
        print(headers)

         # Print each row in the CSV file.
        for row in file_reader:
                
                #2. Add to the toal vote count
                total_votes += 1

# 3. Print the toal votes
print(total_votes)
