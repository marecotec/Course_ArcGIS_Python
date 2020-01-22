
#####
# Step 2 - sys - system
#####

# The system package gives you functions that allow you to interface with Python irrespective of the
# platform we are using.
import sys

# For example, we can find out the version of the software:
print sys.version

# Locate our Python Executable path
print sys.executable

# Read and write to the interpreter directly (similar to print function, but a bit more powerful)
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

# Perhaps the most important function is sys.argv, which will allow you to add commands to the interpreter
# from an external file. I use this when executing my Python code from a *.bat file, as you can write:
# C:\Python27\ArcGIS10.5\python.exe Step_2.py ARGUMENT1 ARUGMENT2 Try executing the Step_2.bat file that I have
# provided

def main(arg):
    print("My argument: " + str(arg))
main(sys.argv[1])

# Task - Using sys.argv write a small code block to read in 3 arguments to your Python file
# store each one in a list and iterate through them, printing each with the text "Argument 1 = ", "Argument 2 = ".
# Hint, you will need to edit the *.bat file to include the arguments.

# Bonus Task 2 - Code your Scrabble score work from Coding Challenge 2 to use 3 sys.argv inputs