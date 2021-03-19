
#####
# Step 1 - Searching directories for files and list them
#####

# Handling files is a critical part of any GIS (and analysis) workflow. This is particularly true if you are
# working with large amounts of files as we often do. In this step, we cover several ways of searching and
# listing files. We will use a mix of different methods and packages to do this. There are no right or
# wrong ways, providing you get the data you require.

# Part 1 - List files in the Step_1 directory using glob.glob: https://docs.python.org/2/library/glob.html

import glob
import os

# List all Python files in current directory
print(glob.glob("*.py"))
# Change to parent of current directory (dangerous as you might struggle to change it back later...)
os.chdir("../")
print(glob.glob("*")) # no pattern match, lists all folders and files
# If you changed directory, you may need to change it back:


# Part 2 - List files using os (more painful)
all = os.listdir(os.curdir)# files and directories
print(all)
files = filter(os.path.isfile, os.listdir(os.curdir))  # files only, might not find anything
print(files)

for file in os.listdir(os.curdir):
    if file.endswith(".shp"):
        print(file)

# Part 3 - List files using arcpy, note: all will return None
import arcpy

# ListFiles ({wild_card}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfiles.htm
print(arcpy.ListFiles("*"))

# ListDatasets ({wild_card}, {feature_type}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
print(arcpy.ListDatasets("*",  "Feature"))
# ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfeatureclasses.htm
print(arcpy.arcpy.ListFeatureClasses("*"))

# ListRasters ({wild_card}, {raster_type})  https://pro.arcgis.com/en/pro-app/arcpy/functions/listrasters.htm
print(arcpy.ListRasters("*", "TIF"))


# Tasks
# 1 - Using the supplied data in Step_1.zip (extract to a folder named Step_1), do the following:
# Hint, you should change your directory to Step_1
import arcpy
os.chdir("CHANGE TO YOUR DIR")
arcpy.env.workspace = "CHANGE TO YOUR DIR"

# a - List and count all shapefiles, how many are there?

# b - List and count all csv, how many are there?

# c - List and count all folders, how many are there?

# d - List and count all rasters in GRID format, how many are there?

# e - List and count all rasters in TIF format, how many are there?

# f - List and count all folders beginning with the letter/character S_, how many are there?

