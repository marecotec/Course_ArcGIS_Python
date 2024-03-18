
#####
# Step 5 - Using functions in arcpy
#####

# When would you use a function in arcpy? Let's say you want to query several datasets using describe, and return
# a series of variables, you'd have to code the arcpy.Describe output several times. It's far easier to code a
# single function and from there, we can send a dataset to it multiple times:

# import arcpy
#
# def describe_shp(input_shapefile):
#     if arcpy.Exists(input_shapefile):
#         desc = arcpy.Describe(input_shapefile)
#         print("Describing: " + str(input_shapefile))
#         if desc.dataType == "ShapeFile":
#             print("Feature Type:  " + desc.shapeType)
#
#         else:
#             print("Input data not ShapeFile..")
#     else:
#         print("Dataset not found, please check the file path..")
#
#
# input_shapefile = "C:\Course_ArcGIS_Python\8_Functions\Step_5_Data\Places.shp\Places.shp"
# describe_shp(input_shapefile)

# Task 1 - Using the Places.shp provided, extend the describe_shp function to include the following outputs: 1) Coordinate system used, 2) Coordinate system type
# Hint: you can find these at https://pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm, and print them out in a well formatted style.

import arcpy

def describe_shp(input_shapefile):
    desc = arcpy.Describe(input_shapefile)
    print("Describing: " + str(input_shapefile))
    if arcpy.Exists(input_shapefile):
        if desc.dataType == "ShapeFile":
            print("Feature Type:  " + desc.shapeType)
            print("Coordinate System Type:  " + desc.spatialReference.type)
            print("Coordinate System used:  " + desc.spatialReference.GCSName)
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")


input_shapefile = r"C:\Data\Course_ArcGIS_Python\Classes\08_Functions\DataFolder_Step_5_Data\Places.shp"
describe_shp(input_shapefile)

# Task 2 - Run your function on the RI_Roads.shp dataset, use only 1 line of code.
describe_shp(r"C:\Data\Course_ArcGIS_Python\Classes\08_Functions\DataFolder_Step_5_Data\RI_Roads.shp")
