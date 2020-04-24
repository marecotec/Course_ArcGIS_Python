
#####
# Step 0 - Practice tasks before we start.
#####

# Express these items as a list using list append (i.e. .append) and print it:

item1 = "woodlands.shp"
item2 = "marshlands.shp"
item3 = "beaches.shp"

file_list = []

file_list.append(item1)
file_list.append(item2)
file_list.append(item3)

print file_list

# How many files are in the list?

print len(file_list)

# Take this list of files (file_list), and using a for loop, go through each file name and change
# the file extension from shp to csv and print new_extension_file_list.

new_extension_file_list = []

for file in file_list:
    file_name = file.split(".")
    new_extension_file_list.append(file_name[0] + ".csv")

print new_extension_file_list