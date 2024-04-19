#####
# Step 4 - Data Access module - Adding new records using an InsertCursor.
#####

# Insert Cursors are used to add new data to shapefile or feature class. It is almost exactly the same
# as the other Cursors that we have used. In this example, we will construct a line feature class.

import arcpy, os
from math import radians, sin, cos

# # Create an empty Shapefile
# arcpy.env.workspace = r"C:\Course_ArcGIS_Python\Classes\9_Cursors"
#
# # Set local variables
# out_path = arcpy.env.workspace
# out_name = "radiating_line.shp"
# geometry_type = "POLYLINE"
# template = "#"
# has_m = "DISABLED"
# has_z = "DISABLED"
#
# # Use Describe to get a SpatialReference object
# spatial_ref = 4326
#
# # Execute CreateFeatureclass
# arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
#                                     has_m, has_z, spatial_ref)
#
#
# # From a point (origin), let's create some radiating lines and add them to the new shapefile
#
# origin_x, origin_y = (-71.42,  41.47)
# distance = 1
# angle = 10  # in degrees
#
# OutputFeature = os.path.join(out_path, out_name)
#
# #create list of bearings
# angles = range(0, 360,angle)
#
#
# for ang in angles:
#     # calculate offsets with  trig
#     angle = float(int(ang))
#     (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
#     (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
#     (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)
#
#     cur = arcpy.InsertCursor(OutputFeature)
#     lineArray = arcpy.Array()
#
#     # start point
#     start = arcpy.Point()
#     (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
#     lineArray.add(start)
#
#     # end point
#     end = arcpy.Point()
#     (end.ID, end.X, end.Y) = (2, end_x, end_y)
#     lineArray.add(end)
#
#     # write our fancy feature to the shapefile
#     feat = cur.newRow()
#     feat.shape = lineArray
#     cur.insertRow(feat)
#
# 	# yes, this shouldn't really be necessary...
#     lineArray.removeAll()
#     del cur


# Task - Using the above code, amend it so you can do multiple origin_x and origin_y. Note that you don't have to do
# too much to the code, so think of the steps you need to take before you touch this. BTW this is a hard one. Use this
# for your input locations: input_locations = [(-71.42,  41.47), (-72.42,  42.47), (-73.42,  43.47)]

import arcpy, os
from math import radians, sin, cos

# Create an empty Shapefile
arcpy.env.workspace = r"H:\NRS528_2024\1_Class_Files\Classes\09_Cursors"

# Set local variables
out_path = arcpy.env.workspace
out_name = "radiating_line_2.shp"
geometry_type = "POLYLINE"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_ref = 4326

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)


input_locations = [(-71.42,  41.47), (-72.42,  42.47), (-73.42,  43.47)]

for i in input_locations:

    origin_x, origin_y = i[0], i[1]
    distance = 1
    angle = 10  # in degrees

    OutputFeature = os.path.join(out_path, out_name)

    #create list of bearings
    angles = range(0, 360, angle)


    for ang in angles:
        # calculate offsets with  trig
        angle = float(int(ang))
        (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
        (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
        (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)

        cur = arcpy.InsertCursor(OutputFeature)
        lineArray = arcpy.Array()

        # start point
        start = arcpy.Point()
        (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
        lineArray.add(start)

        # end point
        end = arcpy.Point()
        (end.ID, end.X, end.Y) = (2, end_x, end_y)
        lineArray.add(end)

        # write our fancy feature to the shapefile
        feat = cur.newRow()
        feat.shape = lineArray
        cur.insertRow(feat)

        # yes, this shouldn't really be necessary...
        lineArray.removeAll()
        del cur

