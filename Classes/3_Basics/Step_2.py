
#####
# Step 2 - Commenting in Python
#####

# You can list packages using the code:
help("modules")

# Importing packages is easy:
import arcpy
arcpy.AddMessage(r'arcpy loaded!\n')

# You can also change the name of the package you load into something else:
import arcpy as arcpython
arcpython.AddMessage(r'I changed the name of arcpy\n')

# You can import more than one package at once:
import arcpy, os
arcpy.AddMessage(os.listdir(r'c:'))

# You can also be selective in your loading of various packages by using from:
from arcpy import AddMessage
arcpy.AddMessage(r'I only loaded AddMessage')




