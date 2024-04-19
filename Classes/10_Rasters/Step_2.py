
#####
# Step 2 - Rasters and numpy
#####

# Numpy is an exceptionally powerful package for Python that gives incredible scientific computing functionality.
# Some basic functionality has been built into arcpy that allows us to interact with it in a fairly seamless manner.

# Review the code below, this is a simple conversion that we are doing, converting Meters to Feet in an elevation
# raster. Of course, you could do this using Raster Calculator, but what if you want to do more complex statistics,
# model simulations and so on?

# Be aware that the size of the raster is crucial as the resulting numpy array will reside in your computer
# memory, so no 10gb files if you only have 8gb of RAM!

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"H:\NRS528_2024\1_Class_Files\Classes\10_Rasters\Step_2_Data"

inRas = arcpy.Raster("etopo10")
lowerLeft = arcpy.Point(inRas.extent.XMin, inRas.extent.YMin)
cellSize = inRas.meanCellWidth
arr = arcpy.RasterToNumPyArray(inRas, nodata_to_value=0)

# Print the resulting array
print(arr.shape)
print(arr)

# Now lets convert m to feet
arrFeet = arr * 3.28084

print(arrFeet)

newRaster = arcpy.NumPyArrayToRaster(arrFeet, lowerLeft, cellSize, value_to_nodata=0)
newRaster.save("etopo10_ft.tif")

# # Task: Using the etopo10 dataset and a NumPyArray, extract only land values, replacing them with null data and
# # create the resulting tif file. Hint: arr[arr < 0] = -9999, where -9999 is a null value

