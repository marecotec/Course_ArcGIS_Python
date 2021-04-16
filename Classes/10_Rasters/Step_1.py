
#####
# Step 1 - Zonal stats and extracting values to points
#####

# Raster processing in arcpy is very similar to working with shapefiles and other feature classes. In this example, we
# conduct some zonal statistics and undertake point value extraction from a raster.

# Using Step_1_Data.zip, extract the zonal values for the shapefile: Biogeography_Made_Up.shp, and the sst_mean.tif
# raster.
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Data\Course_ArcGIS_Python\Classes\10_Rasters\DataFolder\Step_1_Data"
arcpy.gp.ZonalStatisticsAsTable_sa("Biogeography_Made_Up.shp", "Area", "sst_mean.tif", "sst_mean_zones.dbf", "DATA", "ALL")

# Pulling values from a raster using a point shapefile is also pretty easy, this time, we use the Extract Values tool.
arcpy.gp.ExtractValuesToPoints_sa("Great_Whites.shp", "sst_mean.tif", "Great_Whites_Extract.shp", "NONE", "VALUE_ONLY")

# Task 1 -  Using a for loop, process all three *.tif files for SST (mean, min and max), you will need to edit the code from lines 11-15 above.
# HInt: ZonalStats... is sensitive to file name output, you may need to use something that shortens the output table name:
# e.g. file_name = raster[:6] + "_out.dbf"

# Task 2 - I want you to run the tool above on the rasters provided (mean, min and max). Think about how you will do this,
# maybe search online about extracting multiple values to points, is here a different tool available to the above that
# allows for multiple inputs?