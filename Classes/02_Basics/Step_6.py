
#####
# Step 6 - Using Functions to block code
#####

# A simple function:
def square(x):
    y = x ** 2
    return y

print(square(3))
print(square(8347329))

# Function with multiple arguments
def string_parser(string, n):
    while string:
        yield string[:n]
        string = string[n:]
print(list(string_parser("1234567890",2)))

