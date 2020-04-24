
#####
# Step 1 - os - operating system
#####

# The os package gives you functions that allow you to interface with the operating system:
import os

# Part a - Executing a Shell/Command Prompt command
os.system("dir") #DIR is a Windows command to list contents of current directory
# Other notable commands - mkdir = make directory, rmdir = delete directory

# Task - Use os.system to make a directory in your current directory, check if it is created
# delete it and check again.

# Part b - Other interesting functions you can use within Python
path = r"test_dir"

# Create a directory
os.mkdir(path)

# Return a list of the entries in the directory given by path.
list = os.listdir(path)
print list

# Rename the file or directory src to dst.
os.rename("test_dir", "test_dir2")

# Remove directories recursively.
os.removedirs(path + "2")

# # Remove (delete) the file path.
os.remove(path)

# # Remove (delete) the directory path.
os.rmdir(path)

# Bonus Task 2 - Use os to make a directory in your root directory, add a subdirectory inside it, check if it is created,
# delete the subdirectory and the main directory. Check if the main directory exists, print "namrdir EXISTS" or "namrdir NOT EXISTS"