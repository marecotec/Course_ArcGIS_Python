
#####
# Step 2 - Querying your data, extent, cell size, type etc
#####

# Part a - What are you?

# Extract Step_2_data.zip into a folder of known location.

#  Below is example code that interrogates a shapefile and returns the type of data stored within it:
import arcpy
desc = arcpy.Describe(r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy\DataFolder_Step_3_data\Places_Been.shp")

# Describe returns a "Describe" object, which basically has multiple properties that we can query.
print(desc) # Returns meaningless information - geoprocessing describe data object...
print(desc.shapeType) # Providing you supply the same shapefile as me, you will get "point", for more info
# see this link: http://pro.arcgis.com/en/pro-app/arcpy/functions/featureclass-properties.htm

print(desc.extent)
# Print a more accessible spatialReference output (this uses string substitution notation:
print("Extent:\n  XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))

print(desc.spatialReference) # Returns meaningless information - geoprocessing spatial reference object, we need to go deeper
print(desc.spatialReference.name)
print(desc.spatialReference.type)

# Task 1 - Using the raster dataset supplied - 0320001450.JP2, extract the following information (Hint you may
# need to use r"file path" due to the \ in the filename), using substitution notation to format this nicely e.g.
# print("Dataset type: %s" % desc_image.datasetType)
# 1. Dataset Type
# 2. Spatial Reference Name, Type and Unit (hint: http://pro.arcgis.com/en/pro-app/arcpy/classes/spatialreference.htm)
# 3. Get min Y and max Y extent
# 4. Get cell size of X and Y (hint: https://community.esri.com/thread/20092)
# 5. Get number of bands (hint: http://pro.arcgis.com/en/pro-app/arcpy/functions/raster-dataset-properties.htm)

#First Describe image
desc_image = arcpy.Describe(r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy\DataFolder_Step_3_data\0320001450.JP2")
# 1. Dataset Type
print("Dataset Type: %s" % desc_image.datasetType)
# 2. Spatial Reference Name and Type.
print("Spatial Reference Name: %s" %  desc_image.spatialReference.name)
print("Spatial Reference Type: %s" % desc_image.spatialReference.type)
print("Spatial Unit: %s" % desc_image.spatialReference.linearUnitName)
# 3. Get min Y and max Y extent
print("Extent:\n  YMin: {0},\n YMax: {1}".format(desc_image.extent.YMin, desc_image.extent.YMax))
# 4. Get cell size
print("Cell size X: {0}, Cell size Y: {1}".format(desc_image.children[0].meanCellWidth, desc_image.children[0].meanCellHeight))
# 5. Get number of bands
print("Band Count: %s" % desc_image.bandCount)