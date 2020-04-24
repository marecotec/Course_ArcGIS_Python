
#####
# Step 2 - Making and deleting files and folders
#####

# It is quite common that you will create a large amount of temporary files during the course of a normal
# geoprocessing operation, one way to store physical files is to use temporary directories, which can be removed
# following the successful completion of the processing operation.

import os
import arcpy

input_directory = "CHANGE TO YOUR DIR"
keep_temp_files = True

# In this example,. I show you how to use os.path.join to create directory names, which can be used to
# test if the directory exists, and if not, create it.

if not os.path.exists(os.path.join(input_directory, "species_files")):
    os.mkdir(os.path.join(input_directory, "species_files"))
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))
if not os.path.exists(os.path.join(input_directory, "outputs")):
    os.mkdir(os.path.join(input_directory, "outputs"))

# Deletion of the files can also be controlled using a True or False variable. In this case, I only delete
# the temporary_files and species_files directories. I use arcpy to do this, as if you are generating files
# through arcpy, other methods such as shutil.rmtree will fail due to arcpy file locks.
if keep_temp_files == False:
    arcpy.Delete_management(os.path.join(input_directory, "species_files"))
    arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))



# Task 1 - Using the code above create a temporary folder and an output folder, and adjust the code below to store the
# generated CSV files in the temporary folder, and the generated shapefiles in the output folder. Then delete
# the temporary file folder.

# This code splits a species CSV file, see Step_2.csv, into individual species CSV files, and then converts them into a
# shapefile. You will have to make several changes to the code to make it work, so try your best.

#
# Insert your code here
#

# # Step 1: Lets determine our species
# species_list = []
# with open(os.path.join(input_directory, data_file)) as species_csv:
#     header_line = species_csv.next()
#     for row in csv.reader(species_csv):
#         try: #Using try/except saves us if there is a line with no data in the file
#             if row[0] not in species_list:
#                 species_list.append(row[0])
#         except:
#             pass
# print "..There are: " + str(len(species_list)) + " species to process.."
#
# # Step 2: Lets split the files
# if len(species_list) > 1:
#     for s in species_list:
#         s_count = 1
#         with open(os.path.join(input_directory, data_file)) as species_csv:
#             for row in csv.reader(species_csv):
#                 if row[0] == s:
#                     if s_count == 1:
#                         file = open(os.path.join(input_directory, "species_files", str(s.replace(" ", "_")) + ".csv"), "w")
#                         file.write(header_line)
#                         s_count = 0
#                     #make well formmated line
#                     file.write(",".join(row))
#                     file.write("\n")
#         file.close()
#
#
# # Step 3: Convert those files into Shapefiles
# os.chdir(os.path.join(input_directory, "species_files"))# same as env.workspace
# arcpy.env.workspace = os.path.join(input_directory, "species_files")
# species_file_list = glob.glob("*.csv")# Find all CSV files
#
# count = 0
#
# for species_file in species_file_list:
#     print ".. Processing: " + str(species_file) + " by converting to shapefile format"
#     in_Table = species_file
#     x_coords = "decimalLongitude"
#     y_coords = "decimalLatitude"
#     z_coords = ""
#     out_Layer = "species" + str(count)
#     saved_Layer = species_file.replace(".","_") + ".shp"
#
#     # Set the spatial reference
#     spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
#
#     lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#     arcpy.CopyFeatures_management(lyr, saved_Layer)
#     count = count + 1
#     arcpy.Delete_management(lyr)

#
# Insert your code here
#



