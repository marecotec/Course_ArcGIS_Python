
#####
# Step 2 - Python Script from Tools
#####

# Perhaps one of the most common ways of constructing a Python script, particularly when using
# unfamiliar tools, is to run the tool and to extract the Python code from the "Results" window
# once the tool has successfully run.

# In this example, we will process a directory of Landsat 8 images, by first running the tools
# that we need in ArcMap and Toolbox, we will then extract the Python code from each tool and
# build a Python script around it.

# Task 1 - Using Step_2_data.zip, select the first layer, and execute the tool "Composite Bands" on Winter_2013.
# you will need to composite all the band images (ending in Bn.tif (where n = band number), do not add the BQA.tif
# file. See Landsat 8 band reference - https://landsat.usgs.gov/what-are-best-spectral-bands-use-my-study

# Once the tool has successfully completed, go into the Geoprocessing "Results" window, right click on the
# Completed tool, select "Copy as Python Snippet" and paste the tool output below:

import arcpy

arcpy.CompositeBands_management(in_rasters="D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B1.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B10.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B11.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B2.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B3.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B4.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B5.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B6.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B7.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B8.tif;"
                                           "D:/Python-Class/Class7/Winter_2013/LC08_L1TP_012031_20131212_20170307_01_T1_B9.tif",
                                out_raster="D:/Python-Class/Class7/winter13")


# Task 2 -  Now it is relatively easy to copy this and change the file name in order to run it on the Winter_2014 data
# but we are not going to do that, instead, we can going to use Python to do this for us from a directory name. Below,
# complete the code that I have provided.

arcpy.env.workspace = "D:/Python-Class/Class7/Winter_2014/"
listRasters = arcpy.ListRasters("*", "TIF")
print listRasters

# Remove the BQA.tif file from the list, replace ****** with the correct string.
listRasters = [x for x in listRasters if "_BQA.tif" not in x]
# listRasters = [x for x in listRasters if "******" not in x]
print listRasters

# Now edit the arcpy.CompositeBands_Management tool to run the Winter 2014 data, hint, you can provide the in_rasters
# argument as a list.
print "Compositing Bands... "
arcpy.CompositeBands_management(in_rasters=listRasters, out_raster="D:/Python-Class/Class7/winter14.tif")
print "Compositing Bands... Finished"

# Task 3 - This is difficult, now I want you to batch run the Composite Bands script on all of our Winter_201n
# data. Hint: use the list and starter code I have provided, and consider using a for loop to run through each year of data
# complete the composite bands tool for each one, and go from there.

import os, arcpy
listYears = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]
outputDirectory = "D:/Python-Class/Class7/WinterComposites"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

# Consider what you want to do before you start. 1) for loop through listYears, 2) set your workspace to the correct
# year, 3) arcpy.ListRasters, 4) remove BQA.tif, 5) composite bands into a known location.

for year in listYears:
    arcpy.env.workspace = "D:/Python-Class/Class7/Winter_" + year
    listRasters = arcpy.ListRasters("*", "TIF")
    print "For year: " + year + ", there are: " + str(len(listRasters)) + " bands to process."
    listRasters = [x for x in listRasters if "_BQA.tif" not in x]
    print "Compositing Bands for " + year
    arcpy.CompositeBands_management(in_rasters=listRasters, out_raster=os.path.join(outputDirectory, "Winter" + year + ".tif"))
    print "Compositing Bands for " + year + " finished."

# Task 4 - See Step_3.py for the Task!


