
#####
# Step 3 - Speeding up processes by using In Memory files
#####

# Writing files to disk can often be a bottleneck in performance, especially when working with many smaller files.
# So arcpy provides an in_memory workspace:
# https://pro.arcgis.com/en/pro-app/help/analysis/geoprocessing/basics/the-in-memory-workspace.htm

# There are several limitations of this though, from the ArcGIS website:
## Data written to the in-memory workspace is temporary and will be deleted when the application is closed.
## Tables, feature classes, and rasters can be written to the in-memory workspace.
## The in-memory workspace does not support extended geodatabase elements such as subtypes, domains, representations, topologies, geometric networks, and network datasets.
## Feature datasets or folders cannot be created in the in-memory workspace.

# Example with a Table

import arcpy

directory = r"C:\Data\Course_ArcGIS_Python\Classes\07_File_Handling"

arcpy.env.workspace = directory

table = arcpy.CreateTable_management("in_memory", "table1")
arcpy.AddField_management(table, "Field1", "TEXT", field_length=20)

cursor = arcpy.da.InsertCursor(table, ["Field1"])
cursor.insertRow(["Hello World"])

arcpy.TableToTable_conversion(table, directory, "Step_3_Output.csv")

# Example with a Shapefile

import os

points_list =[[20.000,43.000],[25.500, 45.085],[26.574, 46.025], [28.131, 48.124]]
pt = arcpy.Point()
ptGeoms = []
for p in points_list:
    pt.X = p[0]
    pt.Y = p[1]
    ptGeoms.append(arcpy.PointGeometry(pt))

arcpy.CopyFeatures_management(ptGeoms, "in_memory/points")

# Lets do something with the shapefile, just print the OID
field = "OID"
cursor = arcpy.SearchCursor("in_memory/points")
row = cursor.next()
while row:
    print(row.getValue(field))
    row = cursor.next()

arcpy.CopyFeatures_management("in_memory/points", os.path.join(directory, "Step_3_shp_output.shp"))


# Task 1 - Create an in_memory shapefile with the locations, points_list =[[20.000,43.000],[25.500, 45.085],[26.574, 46.025], [28.131, 48.124]]
# add new fields- Location, Species, and populate those fields for each row (for this example, each row should contain the same data
# eg Location = World, Species = Phragmites. When done, export the shapefile to ArcMap.

# The code to add values to the fields for each record is this:
# cur = arcpy.UpdateCursor("in_memory/points1")
# for row in cur:
#     row.setValue('Location', "World")
#     row.setValue('Species', "Phragmites")
#     cur.updateRow(row)


points_list =[[20.000,43.000],[25.500, 45.085],[26.574, 46.025], [28.131, 48.124]]
pt = arcpy.Point()
ptGeoms = []
for p in points_list:
    pt.X = p[0]
    pt.Y = p[1]
    ptGeoms.append(arcpy.PointGeometry(pt))

arcpy.CopyFeatures_management(ptGeoms, "in_memory/points1")
arcpy.AddField_management("in_memory/points1", "Location", "TEXT", field_length=20)
arcpy.AddField_management("in_memory/points1", "Species", "TEXT", field_length=20)

cur = arcpy.UpdateCursor("in_memory/points1")
for row in cur:
    row.setValue('Location', "World")
    row.setValue('Species', "Phragmites")
    cur.updateRow(row)

arcpy.CopyFeatures_management("in_memory/points1", os.path.join(directory, "Step_3_shp_output_Species.shp"))