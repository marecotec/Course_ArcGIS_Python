
#####
# Step 0 - Practice tasks before we start.
#####

# Task a: Split the following strings into lists (hint: you may need to use ".split()".

stringWords = "hi;hello;goodbye;au revoir"
##### add the result to a list named "listWords":

listNumbers = "1 2 3 4 5"
##### add the result to a list named "listNumbers":

# Task b: Using a for loop, do the following:

##### Count the number of characters in each word in listWords (hint: len()), print the word and
# the sum and calculate a sum of all words. Look out for typeError, i.e. trying to print an int as
# part of a string. Total number should be 23.

##### Using a for loop (hint: you will need two loops), multiply every value in listNumbers by every
# value in this list multiplyNumbers = [89, 28, 31] and calculate the sum. Answer = 2220. Hint:
# you may find that you get a typeError, so ensure you convert your listNumber number into int using:
# int(str(number))

# Task c: Read the contents of the csv file supplied (Step_0_Commands.csv) into four variables, that we
# can use to program an extent environment. I have provided some starter code. Hint, you will need to use CSV.

# import csv
#
# with open("Step_0_Commands.csv") as command_csv:
#     csv_reader = csv.reader(command_csv, delimiter=',')
#
#     for row in csv_reader:
#         if row[0] == "extent_s":
#             YMin = row[1]
#
# print("Extent:\n XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(XMin, XMax,YMin,YMax))
