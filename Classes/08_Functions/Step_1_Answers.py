
#####
# Step 1 - Basic Functions
#####

# Functions are a fundamental coding tool in Python, they enable you to create blocks of
# code that can be repeatably used. Once written you can talk to the function multiple times
# with different inputs.

# Functions are defined using "def", followed by the function name and arguments in parentheses.
# the first line can be an optional statement that contains documentation about the function,
# aka docstring. Functions may have a "return" argument, which may return an output of the
# function but this is not essential. To call a function you would call the name of the function
# and provide the arguments, see the example below.


def do_math(x,y):
    """This is docstring, it can be used to explain what the function does."""
    value = x + y
    return value


print do_math(1, 2)


# Task 1 - Comment out the above code (lines 15-21), and then execute the below code, analyze the error,
# why did the code below not work?

def print_me( str ):
    """This prints a passed string into this function"""
    print str
    return


print_me()

# Task 2 - Repair the code in the area below (Hint: do you need to edit the function or not?):

print_me("Ha ha!")


# Task 3 - Turn the code below into a function, and then run the code using the inputs: a and b (shown), and
# s and e

i = "a"
j = "b"

output = i + j + j + i
print output

def word_maker(i,j):
    output = i + j + j + i
    print output
    return

word_maker("a", "b")
word_maker("s", "e")

