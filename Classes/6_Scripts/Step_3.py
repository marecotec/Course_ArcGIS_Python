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

