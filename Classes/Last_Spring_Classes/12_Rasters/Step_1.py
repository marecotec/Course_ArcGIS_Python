
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
arcpy.env.workspace = r"Z:\Andy's Documents\Teaching and students\URI\NRS - GIS Python Course\Github\Course_ArcGIS_Python\Classes\12_Rasters\Step_1_Data"
arcpy.gp.ZonalStatisticsAsTable_sa("Biogeography_Made_Up.shp", "Area", "sst_mean.tif", "sst_mean_zones.dbf", "DATA", "ALL")

# Task 1 -  Using a for loop, process all three *.tif files for SST (mean, min and max), you will need to edit the code above.
# HInt: ZonalStats... is sensitive to file name output, you may need to use something that shortebs the output table name:
# e.g. file_name = raster[:6] + "_out.dbf"



# Pulling values from a raster using a point shapefule is also pretty easy, this time, we use the Extract Values tool.

arcpy.gp.ExtractValuesToPoints_sa("Great_Whites.shp", "sst_mean.tif", "Great_Whites_Extract.shp", "NONE", "VALUE_ONLY")

# Task 2 - I want you to run the tool above on the rasters provided (mean, min and max). Think about how you will do this,
# maybe search online about extracting multiple values to points.

