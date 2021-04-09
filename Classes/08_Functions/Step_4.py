
#####
# Step 4 - Anonymous Functions - Lambda
#####

# Rather than using def, you can also define simple functions using the lambda keyword. These are called
# "anonymous" as you are not defining the function using def. The syntax is the keyword lambda, followed
# by the input arguments, a colon ":", and then the function.

# Example 1
sum = lambda in1, in2: in1 + in2
print("Value = ", sum(10, 20))

# Exzample 2
x = lambda a, b, c: a + b + c
print("Value = ", x(5, 6, 2))

# Task 1 - Using lambda, write a function to return the cube of a number (x*x*x).

cube = lambda x: x*x*x
print("Value = ", cube(2))


def cube_of_number(x):
    return x * x * x
print(cube_of_number(3))