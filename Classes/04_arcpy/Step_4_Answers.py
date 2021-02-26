
#####
# Step 4 - Environments
#####

# Environments in script tools are like environments in any other tool, environment
# values are passed down to the script tool, where they are automatically applied to
# any tools run within the script. You can also set environments within a script tool,
# thereby overriding any passed-down environments. Environment values set within scripts
# only apply to the execution of the script.

# For example, you may already be familiar with the Current and Scratch workspace
# environment settings, which allow you to set workspaces for inputs and outputs. Another
# example is the Extent environment setting, which allows your analysis to be limited to
# a specific geographic area, or the Output Coordinate System environment setting, which
# defines the coordinate system (map projection) for new data.

# There are a lot of options, see the link for more details:
# http://desktop.arcgis.com/en/arcmap/10.5/tools/environments/what-is-a-geoprocessing-environment.htm

# Part a - Setting Current and Scratch Workspaces

# workspace = http://desktop.arcgis.com/en/arcmap/10.5/tools/environments/current-workspace.htm
# scratchWorkspace = http://desktop.arcgis.com/en/arcmap/10.5/tools/environments/scratch-folder.htm

import arcpy

# Print the passed-down current workspace environment setting
arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)

# Set a new workspace, overriding the passed-down workspace
arcpy.env.workspace = r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy"
arcpy.env.scratchWorkspace = r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy"
arcpy.AddMessage("The new current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The new scratch workspace is: %s" % arcpy.env.scratchWorkspace)


# Task 1 - Set the geoprocessing environment extent to, hint: find the command needed at this link:
# http://desktop.arcgis.com/en/arcmap/10.5/tools/environments/what-is-a-geoprocessing-environment.htm
# Top - 147999.685356
# Bottom - 147554.685356
# Left - 320172.363053
# Right - 320778.363053
# BTW, we are using the spatial reference: NAD_1983_Rhode_Island_ft for this exercise

arcpy.env.extent = arcpy.Extent(320172.363053, 147554.685356, 320778.363053, 147999.685356)

# Task 2 - With the environment set undertake a simple processing operation on the data provided
# in Step_4_data.zip by editing the code:
# input_raster = r""
# output_workspace = ""
# raster_format = "TIFF"
# arcpy.RasterToOtherFormat_conversion(input_raster, output_workspace, raster_format)

input_raster = r"D:\Python-Class\Class5Step4\0320001450.JP2"
output_workspace = r"D:\Python-Class"
raster_format = "TIFF"
arcpy.RasterToOtherFormat_conversion(input_raster, output_workspace, raster_format)





