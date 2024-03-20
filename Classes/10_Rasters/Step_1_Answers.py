
#####
# Step 1 - Zonal stats and extracting values to points
#####

# Raster processing in arcpy is very similar to working with shapefiles and other feature classes. In this example, we
# conduct some zonal statistics and undertake point value extraction from a raster.

# Using Step_1_Data.zip, extract teh zonal values for the shapefile: Biogeography_Made_Up.shp, and the sst_mean.tif
# raster.
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"H:\NRS528_2024\1_Class_Files\Classes\10_Rasters\Step_1_Data"

# Task 1 -  Using a for loop, process all three *.tif files for SST (mean, min and max), you will need to edit the code above.
# HInt: ZonalStats... is sensitive to file name output, you may need to use something that shortebs the output table name:
# e.g. file_name = raster[:6] + "_out.dbf"

# raster_list = arcpy.ListRasters()
#
# for raster in raster_list:
#     file_name = raster[:6] + "_out.dbf"
#     arcpy.gp.ZonalStatisticsAsTable_sa("Biogeography_Made_Up.shp", "Area", raster, file_name, "DATA",
#                                        "ALL")

# # Pulling values from a raster using a point shapefule is also pretty easy, this time, we use the Extract Values tool.
#
# arcpy.gp.ExtractValuesToPoints_sa("Great_Whites.shp", "sst_mean.tif", "Great_Whites_Extract.shp", "NONE", "VALUE_ONLY")
#
# # Task 2 - I want you to run the tool above on the rasters provided (mean, min and max). Think about how you will do this,
# # maybe search online about extracting multiple values to points.
#
raster_list = arcpy.ListRasters()
arcpy.gp.ExtractMultiValuesToPoints("Great_Whites.shp", raster_list, "BILINEAR")