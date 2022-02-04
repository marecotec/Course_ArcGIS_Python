
#####
# Step 5 - Code cleanliness
#####

# This will trigger an indentation error, but luckily your error will be helpful in figuring out where the fix is
i = 0
while i < 10:
i = i+1
print(i)

# Fix the following code, using the appropriate indentation, you want to produce the following result:
# n = 1
# n = 2
# n = 3
# n = 4
# n = 5 <---
# n = 5
# n = 6 <---
# n = 6
# n = 7

try:
n = 1
while n < 10:
if n == 5:
print('n = 5 <---')
else:
if n == 6:
print('n = 6 <---')
print('n = ' + str(n))
n = n + 1
except:
print('my code failed')
