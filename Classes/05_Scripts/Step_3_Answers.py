#####
# Step 3 - Executing multiple tools - and automating most of it
#####

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Birds.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated shapefile.

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degree.

# 4. Undertake a Spatial Join to join the fishnet to the observed points.

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

# 6. Visualize in ArcMap

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:

import arcpy
arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open.


# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.
arcpy.env.workspace = r"C:\Data\Course_ArcGIS_Python\Classes\05_Scripts"

in_Table = r"Step_3_Cepphus_grylle.csv"
x_coords = "lon"
y_coords = "lat"
out_Layer = "cepphus"
saved_Layer = r"Step_3_Cepphus_Output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Print the total rows
print(arcpy.GetCount_management(out_Layer))
# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated shapefile.

desc = arcpy.Describe(saved_Layer)
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degree.


arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "Step_3_Fishnet.shp"  # Name of output fishnet

# Set the origin of the fishnet
originCoordinate = str(XMin) + " " + str(YMin)  # Left bottom of our point data
yAxisCoordinate = str(XMin) + " " + str(YMin + 1)  # This sets the orientation on the y-axis, so we head north
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = "" # Leave blank, as we have set cellSize
oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

if arcpy.Exists(outFeatureClass):
    print("Created Fishnet file successfully!")


# 4. Undertake a Spatial Join to join the fishnet to the observed points.

target_features="Step_3_Fishnet.shp"
join_features="Step_3_Cepphus_Output.shp"
out_feature_class="Step_3_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..

if arcpy.Exists(out_feature_class):
    print("Created Heatmap file successfully!")
    print("Deleting intermediate files")
    # arcpy.Delete_management(target_features)
    # arcpy.Delete_management(join_features)



