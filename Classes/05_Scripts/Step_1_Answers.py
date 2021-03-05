#####
# Step 1 - Executing and reporting tool outputs
#####

# Part a - convert CSV to shapefile

# Help on Tool: http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/make-xy-event-layer.htm.
# Using the data Step_1_Lionfish.csv, we will use arcpy to convert this to a shapefile.

# import arcpy
# # Set your workspace to the directory where you are storing your files
# arcpy.env.workspace = r"Z:\Andy's Documents\Teaching and students\URI\NRS - GIS Python Course\Github\Course_ArcGIS_Python\Classes\6_Scripts"
#
# in_Table = r"Step_1_Lionfish.csv"
# x_coords = "X"
# y_coords = "Y"
# z_coords = ""
# out_Layer = "lionfish"
# saved_Layer = r"Step_1_Lionfish_Output.shp"
#
# # Set the spatial reference
# spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # Print the total rows
# print(arcpy.GetCount_management(out_Layer))
#
# # Save to a layer file
# arcpy.CopyFeatures_management(lyr, saved_Layer)
#
# if arcpy.Exists(saved_Layer):
#     print "Created file successfully!"


# Tasks - Using the file provided "Step_1_Deep_Coral.csv", undertake the following: Hint: spatial reference is WGS84.

##### 1. Convert the file to a shapefile.

import arcpy
# Set your workspace to the directory where you are storing your files
arcpy.env.workspace = r"C:\Data\Course_ArcGIS_Python\Classes\05_Scripts"

in_Table = r"Step_1_Deep_Coral.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "corals"
saved_Layer = r"Step_1_Deep_Coral_Output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

##### 2. Count the number of records and check output exists in the file.

# Print the total rows
print(arcpy.GetCount_management(out_Layer))

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

##### 3. Check the correct coordinate system has been applied (Hint: see last week!)

desc = arcpy.Describe(saved_Layer)
print(desc.spatialReference.name)

##### 4. Visualize the file in ArcMap.

# Drag it from explorer into ArcMap
