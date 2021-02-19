
#####
# Step 3 - creating and writing files
#####

# We will undertake some basic file reads and file writes

# Creating a text file
file = open("testfile.txt", "w")

file.write("Hello World\n")
file.write("This is a line in our text file\n")
file.write("and this is another line.\n")
file.close()

# If we create this file again, using different words, you will notice it overwrites:
file = open("testfile.txt", "w")

file.write("Goodbye World\n")
file.write("This is not a line in our text file\n")
file.write("and this is not another line.\n")
file.close()

# You need to be careful with this, as once you close/reopen the file, it will create it as a new one.
# To add to a file, the change is subtle.
file = open("testfile.txt", "a")
file.write("Wooahhh, I am a line added later\n")
file.close()

# Reading files is easy, but again a subtle change:
file = open("testfile.txt", "r")
file_contents = file.read()
print (file_contents)
file.close()

# You can also read a line:
file = open("testfile.txt", "r")
file_contents = file.readlines()
counter = 1
for i in file_contents:
    print(str(counter) + ": " + i.rstrip()) #.rstrip() removes new line characters i.e. \n
    counter = counter + 1
file.close()


# Task - Using the provided text file Task_Step_3.txt, within the Tasks directory, iterate through the
# existing file, and find which line numbers the following words are on: Limpet, Mongoose, Spider monkey,
# Zebra. Hint, you will likely fail to match the whole word, as a new line is appended in the file, so
# as you iterate through each line you should match line.rstrip(), as this removes the \n


