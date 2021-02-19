
#####
# Step 4 - Working with CSV files
#####

# One of the more ubiquitous open data file formats is the CSV file, aka comma separated values.
# They are best because they don't use any proprietary formats, e.g. "Excel", so you can be
# assured that this format will be readable many years from today, even if the software you used
# to create it is list.

# I am assuming that everyone is used to a CSV format, e.g.:
### column 1 name,column 2 name, column 3 name
### first row data 1,first row data 2,first row data 3
### second row data 1,second row data 2,second row data 3

# We will query the file Step_4.csv, a file of population data per year per country:
import csv

with open("Step_4.csv") as population_csv:
    csv_reader = csv.reader(population_csv, delimiter=',')

    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print("Column names are: " + str(row))
            line_count += 1
        line_count += 1

print("Processed " + str(line_count) + " lines.")

# We can do some basic tasks, for example, let's sum the "Population" column

with open("Step_4.csv") as population_csv:
    next(population_csv) #skip first line
    total = 0
    for row in csv.reader(population_csv):
        total += float(row[3]) #3 = 4th column, in this case, population, remember Python uses zero indexing
    print(format(total, 'f')) # format prints as float
    print(total) # without we print as engineering notation
    # Now look at the data, 3 hundred billion? Ah, we have multiple years..

# Task - Using Step_4.csv, complete the following, 1) Make a list of the years and the countries in the dataset,
# how many years and countries are there? 2) Calculate the global population for every year in the dataset.
# 3) Split the global dataset into a file for each country, with the filename the name of the country, in a new
# directory using only Python
