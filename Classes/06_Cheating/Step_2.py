#####
# Step 2 - Python Script from Tools
#####

# Perhaps one of the most common ways of constructing a Python script, particularly when using
# unfamiliar tools, is to run the tool and to extract the Python code from the "History" window
# once the tool has successfully run.

# In this example, we will process a directory of Landsat 8 images, by first running the tools
# that we need in ArcGIS Pro and Toolbox, we will then extract the Python code from each tool and
# build a Python script around it.

# Task 1 - Using Step_2_data.zip, select the first layer, and execute the tool "Composite Bands" on Winter_2013.
# you will need to composite all the band images (ending in Bn.tif (where n = band number), do not add the BQA.tif
# file. See Landsat 8 band reference -
# https://www.usgs.gov/faqs/what-are-best-landsat-spectral-bands-use-my-research?qt-news_science_products=0#qt-news_science_products

# Once the tool has successfully completed, go into the Geoprocessing "History" window, right click on the
# Completed tool, select "Copy as Python Snippet" and paste the tool output below:

# Task 2 -  Now it is relatively easy to copy this and change the file name in order to run it on the Winter_2014 data
# but we are not going to do that, instead, we can going to use Python to do this for us from a directory name. Below,
# complete the code that I have provided.

# Now edit the arcpy.CompositeBands_Management tool to run the Winter 2014 data, hint, you can provide the in_rasters
# argument as a list.

# Task 3 - This is difficult, now I want you to batch run the Composite Bands script on all of our Winter_201n
# data. Hint: use the list and starter code I have provided, and consider using a for loop to run through each year of data
# complete the composite bands tool for each one, and go from there.

import os, arcpy
listYears = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]
outputDirectory = r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\DataFolder_Step_2_data_lfs\Test"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

# Consider what you want to do before you start. 1) for loop through listYears, 2) set your workspace to the correct
# year, 3) arcpy.ListRasters, 4) remove BQA.tif, 5) composite bands into a known location.