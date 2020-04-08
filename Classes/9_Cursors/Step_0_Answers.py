
#####
# Step 0 - Practice tasks before we start.
#####

# Task a: Express the following sequences as lists:

##### Create a list of floats 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, call it "floatList", print it.

floatList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

##### Create a  list of individual words using the sentence: "The lake is a long way from here" and
##### call it "strList", print it.
string = "The lake is a long way from here"
strList = string.split
print strList

# Task b: Using a for loop, do the following:

##### Sum the values of floatList and print result (28.0) using a for loop, yes you can use: print sum(intList),
##### call it floatValue, print it

floatValue = 0
for value in floatList:
    floatValue = floatValue + value
print floatValue





