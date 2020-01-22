#####
# Step 2 - Executing multiple tools
#####

# We will use multiple tools to generate a heatmap, and visualize it in ArcMap.

# Part a - Using the Step_2_Deep_Coral_Data.zip as our extents, we will generate a fishnet
# grid: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-fishnet.htm

import arcpy
# set workspace environment
arcpy.env.workspace = r"Z:\6_Scripts"
# Set coordinate system of the output fishnet
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "Step_2_Fishnet.shp"  # Name of output fishnet

# Set the origin of the fishnet
originCoordinate = "-176.87 -51"  # Left bottom of our point data
yAxisCoordinate = "-176.87 -41"  # This sets the orientation on the y-axis, so we head north
cellSizeWidth = "10"  # 10 degrees
cellSizeHeight = "10"
numRows =  ""  # Leave blank, as we have set cellSize
numColumns = "" # Leave blank, as we have set cellSize
oppositeCorner = "162.0200043 71.34999847" # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# Part b - Count the amount of points in each fishnet cell

# To do this we use a tool called SpatialJoin, relatively simple to set up

target_features="Step_2_Fishnet.shp"
join_features="Step_2_Deep_Coral_Data.shp"
out_feature_class="Step_2_Deep_Coral_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

# Part c - Visualize the file in ArcMap and change the symbology to a heatmap esq style.


# FOR OUR TASK HERE, HEAD TO STEP_3.PY