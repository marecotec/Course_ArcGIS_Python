
#####
# Step 3 - Inside and outside Functions
#####

# Arguments are passed by reference. This means, that if you change what an argument refers to within a function,
# the change also reflects back in the calling function. This is basically local versus global scope. Variables
# defined inside a function are local to that function only and unless saved are not progressed into the global
# scope, basically the entire program.


def changeme(mylist):
   mylist.append(40)
   print("Values inside the function: ", mylist)
   return

mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

# However, if you create a new variable inside a function, this change remains local to the function and does not
# propagate outside of the function, unless you save it.

# def changeme(mylist):
#    mylist = [1, 2, 3, 4]
#    print("Values inside the function: ", mylist)
#    return mylist
#
# mylist = [10, 20, 30]
# changeme(mylist)
# print("Values outside the function: ", mylist)


# Task 1 - Using the code above (lines 25 - 32), I want you to save and print the values from the function changeme,
# i.e. the result would be output = [1, 2, 3, 4].


