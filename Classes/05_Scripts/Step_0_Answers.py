
#####
# Step 0 - Practice tasks before we start.
#####

# Task a: Split the following strings into lists (hint: you may need to use ".split()".

stringWords = "hi;hello;goodbye;au revoir"
##### add the result to a list named "listWords":

listWords = stringWords.split(";")
print(listWords)

stringNumbers = "1 2 3 4 5"
##### add the result to a list named "listNumbers":

listNumbers = stringNumbers.split(" ")
print(listNumbers)

# Task b: Using a for loop, do the following:

##### Count the number of characters in each word in listWords (hint: len()), print the word and
# the sum and calculate a sum of all words. Look out for typeError, i.e. trying to print an int as
# part of a strong. Total number should be 23.

sumWords = 0
for word in listWords:
    print(word + ": " + str(len(word)))
    sumWords = sumWords + len(word)
print("Total number= " + str(sumWords))

##### Using a for loop (hint: you will need two loops), multiply every value in listNumbers by every
# value in this list multiplyNumbers = [89, 28, 31] and calculate the sum. Answer = 2220. Hint:
# you may find that you get a typeError, so ensure you convert your listNumber number into int using:
# int(str(number))

multiplyNumbers = [89, 28, 31]
sumMultiplyNumbers = 0
for num in listNumbers:
    for num2 in multiplyNumbers:
        sumMultiplyNumbers = sumMultiplyNumbers + (int(str(num)) * int(str(num2)))
print(sumMultiplyNumbers)

# Task c: Read the contents of the csv file supplied (Step_0_Commands.csv) into four variables, that we
# can use to program an extent environment. I have provided some starter code. Hint, you will need to use CSV.

import csv

with open("Step_0_Commands.csv") as command_csv:
    csv_reader = csv.reader(command_csv, delimiter=',')

    for row in csv_reader:
        if row[0] == "extent_s":
            YMin = row[1]
    # Here is answer code
        if row[0] == "extent_n":
            YMax = row[1]
        if row[0] == "extent_w":
            XMin = row[1]
        if row[0] == "extent_e":
            XMax = row[1]

print("Extent:\n XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(XMin, XMax,YMin,YMax))

