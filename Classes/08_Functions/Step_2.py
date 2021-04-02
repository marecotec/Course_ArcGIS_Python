
#####
# Step 2 - Keyword arguments and defaults
#####

# You can provide arguments to a function by order, i.e. do_math(x,y), the first argument is x and the
# second is y. But to make life a little easier, you can provide keyword arguments. For example:


def do_math(x, y):
    """This is docstring, it can be used to explain what the function does."""
    value = x / y
    return value

print(do_math(1,2))
print(do_math(2,1))

print(do_math(y=1, x=2))
print(do_math(x=2, y=1))


# As part of your function, you can alsop provide default values, which is useful if you have a commonly used
# variable, for example:

# def do_default_math(x=20, y=5):
#     """This is docstring, it can be used to explain what the function does."""
#     value = x / y
#     return value
#
#
# print(do_default_math())
# print(do_default_math(2,1))

# Task 1 - Convert the following code into a function named word_mixer() using a series of keyword arguments
# as follows word_mixer(first_word = "my", third_word = "is", second_word = "name", name = "andy"), of course,
# feel free to change andy to whatever your name is!

# Turn this into a function
# output = first_word + " " + second_word + " " + third_word + " " + name
# print output
# end function code

word_mixer(first_word = "my", third_word = "is", second_word = "name", name = "andy")
word_mixer(first_word = "my", third_word = "is", second_word = "name", name = "bambi")

