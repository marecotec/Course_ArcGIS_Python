
#####
# Step 1 - arcpy: The arcpy moodule
#####

# Part a - Importing

# The arcpy package gives you access to nearly all ArcGIS functions present in Desktop, and
# we can import arcpy in various ways:

##### Import a single specific tool:
from arcpy import Buffer_analysis as ba

##### Import all tools:
import arcpy

##### We can now refer to the same tool as either:

arcpy.Buffer_analysis() # Imported and referred to by the arcpy.* package naming convention, Buffer_
# analysis() on it's own will not work.

ba() # As we imported the tool specifically as ba, we can refer to it as ba.


# Part a - Time to load

# ##### Below, I want to show you the load speed for a specific tool using
# the time package, note there is no real benefit as arcpy is slow:

# import time
# ba_start_time = time.time()
# from arcpy import Buffer_analysis as ba
# print('It took', time.time()-ba_start_time, 'seconds, to load ba.')

# import time
# arcpy_start_time = time.time()
# import arcpy
# print('It took', time.time()-arcpy_start_time, 'seconds, to load arcpy.')

