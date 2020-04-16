
#####
# Step 2 - Interpolation and routines to conduct validation
#####

# We will interpolate a file of elevations, and use a k-fold validation approach, whereby we will loop through creating
# n interpolations, validate with points that were dropped from the interpolation, and report
# a correlation value using Pandas.

# This is a multi-step process:

# 1) Let's do a random selection, and save the split files in different directories.

import arcpy
import random as random
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
from scipy.stats.stats import pearsonr

arcpy.env.workspace = r"C:\Course_ArcGIS_Python\Classes\10_Rasters\Step_2_Data"
input_data = r"Elevations.shp"

arcpy.env.extent = input_data

kfold = 20 #number of folds
prop_samples = 30 #proportion of points to split
i = 0


# Code Obtained from: https://support.esri.com/en/technical-article/000013141, edited to return 2 outputs
def SelectRandomByPercent (layer, layer2, percent):
    fc = arcpy.Describe(layer).catalogPath
    featureCount = float(arcpy.GetCount_management (fc).getOutput(0))
    count = int(featureCount * float(percent) / float(100))
    if not count:
        arcpy.SelectLayerByAttribute_management (layer, "CLEAR_SELECTION")
        return
    oids = [oid for oid, in arcpy.da.SearchCursor(fc, "OID@")]
    oidFldName = arcpy.Describe(layer).OIDFieldName
    delimOidFld = arcpy.AddFieldDelimiters (layer, oidFldName)
    randOids = random.sample (oids, count)
    oidsStr = ", ".join(map(str, randOids))
    sql = "{0} IN ({1})".format(delimOidFld, oidsStr)
    output1 = arcpy.SelectLayerByAttribute_management(layer, "", sql)
    sql = "{0} NOT IN ({1})".format(delimOidFld, oidsStr)
    output2 = arcpy.SelectLayerByAttribute_management(layer2, "", sql)
    return output1, output2


while i < kfold:
    arcpy.MakeFeatureLayer_management(input_data, "input_data_lyr")
    arcpy.MakeFeatureLayer_management(input_data, "input_data_lyr2")
    output1, output2 = SelectRandomByPercent("input_data_lyr", "input_data_lyr2", prop_samples)
    arcpy.CopyFeatures_management(output1, "elv_" + str(i) + "_test.shp")
    arcpy.CopyFeatures_management(output2, "elv_" + str(i) + "_train.shp")
    arcpy.Delete_management("input_data_lyr")
    arcpy.Delete_management("input_data_lyr2")
    i = i + 1


# 2) Now let's create several surfaces using simple interpolation:

training_shp = arcpy.ListFeatureClasses("*train*")
count = 0

for i in training_shp:
    outIDW = Idw(i, "Elevation", 2000, 2, RadiusVariable(10, 50000))
    outIDW.save("elev_" + str(count) + ".tif")
    count = count + 1



# Task - Now we have run through the generation and partitioning of the input shapefile, and created a
# rudimentary interpolation using IDW. We need to validate the file. You should consider the steps you need to
# undertake to validate each partition. I have given you a run down below:

# 1. You need to list the "test" files, see line 58...
# 2. For each IDW and each test file (they share numbers... so you can use a count variable to iterate this,
#    you need to use ExtractValuesToPoints (in_point_features, in_raster, out_point_features) to pull the test
#    values from the "test" shapefile.
# 3. Use the code I provide below to get yourself a correlation value for the interpolation.

# arr = arcpy.da.FeatureClassToNumPyArray("elev_" + str(count) + "_valid.shp", ["Elevation", "RASTERVALU"])
# print "Interpolation " + str(count) + " correlation = " + str(pearsonr(arr["Elevation"], arr["RASTERVALU"]))

# 4. Store the correlation value (hint the pearsonr outputs a tuple), take the mean of the total k-fold (hint sum / length).

# 5. Take a mean of all the interpolated surfaces you generated and store it as an output (Hint:
# https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/cell-statistics.htm

# 6. Take a standard deviation of all the interpolated surfaces you generated and store it as an output (Hint:
# https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/cell-statistics.htm

# 6. Add clean up code to remove temporary files.

test_shp = arcpy.ListFeatureClasses("*test*")
pearson_values = []
raster_list = []

for fc in test_shp:
    run = fc.split("_")
    arcpy.gp.ExtractValuesToPoints_sa(fc, "elev_" + str(run[1]) + ".tif", "elev_" + str(run[1]) + "_valid.shp", "NONE", "VALUE_ONLY")
    arr = arcpy.da.FeatureClassToNumPyArray("elev_" + str(run[1]) + "_valid.shp", ["Elevation", "RASTERVALU"])
    print "Interpolation " + str(run[1]) + " correlation = " + str(pearsonr(arr["Elevation"], arr["RASTERVALU"]))

    pearson_values.append(pearsonr(arr["Elevation"], arr["RASTERVALU"])[0])
    raster_list.append("elev_" + str(run[1]) + ".tif")

    arcpy.Delete_management("elev_" + str(run[1]) + "_valid.shp")
    arcpy.Delete_management("elv_" + str(run[1]) + "_train.shp")
    arcpy.Delete_management("elv_" + str(run[1]) + "_test.shp")

print "Overall mean: " + str(sum(pearson_values) / float(len(pearson_values)))

outCellStats = arcpy.sa.CellStatistics(raster_list, "MEAN", "DATA")
outCellStats.save("out_surface_mean.tif")

outCellStats = arcpy.sa.CellStatistics(raster_list, "STD", "DATA")
outCellStats.save("out_surface_std.tif")

for i in raster_list:
    arcpy.Delete_management(i)













