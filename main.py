import csv
import os

# Prompt the user to enter the filename
filename = input("Enter the filename (including the .csv extension): ")

# Check if the file exists
if not os.path.isfile(filename):
    # Create an empty file
    with open(filename, "w") as file:
        pass

# Open the file and read its contents
with open(filename, "r") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Print each entry
        print("ID: {}, Name: {}, Cost: {}".format(row[0], row[1], row[2]))
