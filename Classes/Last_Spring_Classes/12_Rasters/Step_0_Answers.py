
#####
# Step 0 - Practice tasks before we start.
#####

# Task a: Run the buffer tool on Step_0_Data.zip/RI_Forest_Health_Works_Project_Points_All_Invasives.shp, with a
# distance of 1 mile:
import arcpy

arcpy.env.workspace = r"Z:\Andy's Documents\Teaching and students\URI\NRS - GIS Python Course\Github\Course_ArcGIS_Python\Classes\12_Rasters\Step_0_Data"

arcpy.Buffer_analysis("RI_Forest_Health_Works_Project_Points_All_Invasives.shp",
                      "RI_Forest_Health_Works_Project_Points_All_Invasives_Buffer.shp",
                      "1 mile")

# Task b: Dissolve your resulting buffer:
arcpy.Dissolve_management("RI_Forest_Health_Works_Project_Points_All_Invasives_Buffer.shp",
                          "RI_Forest_Health_Works_Project_Points_All_Invasives_Dissolve.shp")


# Task c: On the original point file (RI_Forest_Health_Works_Project_Points_All_Invasives.shp), use a
# search cursor to print the "Owner" field within the attributes.

input_shp = "RI_Forest_Health_Works_Project_Points_All_Invasives.shp"
fields = ['Owner']

with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        print(u'Owner = {0}'.format(row[0]))

