
#####
# Step 4 - Iteration
#####

# For Loops

# For loop on string
my_string = 'abcde'
for i in my_string:
    print(i)

# For loop on list
my_list = ['a', 'b', 'c', 'd', 'e']
for i in my_list:
    print(i)

# For loop on tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')
for i in my_tuple:
    print(i)

# For loop on dictionary
my_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i, j in my_dictionary.items():
    print(i, j)


# If/else/elif

# You can use if/else/elif to make decisions based on your data:
my_var = 4
if my_var > 6:
    print('Greater than 6')
elif my_var == 5:
    print('Equal to 5')
else:
    print('Less than 5')

# Using if to catch cases as we loop:
my_if_list = [1, 2, 3, 4, 5, 6]
for i in my_if_list:
    if i % 2 == 0:
        print(str(i) + ' is even because we can divide it by two')
    else:
        print(str(i) + ' is odd because it will not divide by two')


# While

# We can use while to perform some task
i = 0
while i < 10:
    i = i+1
    print(i)

# Be careful though not to enter an infinite loop as you forgot your increment
i = 0
while i < 10:
    print(i)


