
#####
# Step 3 - Data Access module - Updating values using a cursor.
#####

# Update cursors are used to adjust data within existing rows of data. You can convert null to non-null values
# or add in calculated values as required.

# Below we use an UpdateCursor to manipulate our data based on two criteria, 1) what the fclass of the road is
# and 2) what the current maxspeed is. We want to set 'residential' roads that have a current max speed of 0
# to 25 (mph).

import arcpy

input_shp = r'H:\NRS528_2024\1_Class_Files\Classes\09_Cursors\Step_3_Data\URI_Campus_Roads_OSM.shp'

fields = ['fclass', 'name', 'maxspeed']

expression = arcpy.AddFieldDelimiters(input_shp, "fclass") + " = 'residential'" + " AND "
expression = expression + arcpy.AddFieldDelimiters(input_shp, "maxspeed") + " = 0"

print("Executing UpdateCursor using Expression: " + expression)

# First let's see if our code works..
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
#
# # # # Run the update
# with arcpy.da.UpdateCursor(input_shp, fields, expression) as cursor:
#     for row in cursor:
#         row[2] = 25
#         cursor.updateRow(row)
#         print("Updated..." + str(row))
#
# expression = arcpy.AddFieldDelimiters(input_shp, "fclass") + " = 'residential'" + " AND "
# expression = expression + arcpy.AddFieldDelimiters(input_shp, "maxspeed") + " = 25"
#
# # # Check, should return no results
# with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
#     for row in cursor:
#         print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))

# Task a - Due to students frequently abusing Segways, the University has set all 'paths' to a speed limit of
# 10 mph. Update URI_Campus_Roads_OSM.shp.

# # Task b - Mooresfield Road has been reclassified to 40 mph, correct this in the data file.
