
#####
# Step 3 - Make your own Python Toolbox!
#####

# Task - Using the code I provide below (basically , including the parameters that I have prepared for you (note, you can
# find all the Python Toolbox Parameters here:
# http://desktop.arcgis.com/en/arcmap/10.3/analyze/creating-tools/defining-parameters-in-a-python-toolbox.htm)

# I want you to attempt to construct a working Python Toolbox. Hint the code is the same as we used before for the
# traditional toolbox, however, I have changed how the arguements are provided to the tool.

# Code for parameters function
params = []
input_line = arcpy.Parameter(name="input_line",
                             displayName="Input Line",
                             datatype="DEFeatureClass",
                             parameterType="Required",  # Required|Optional|Derived
                             direction="Input",  # Input|Output
                             )
input_line.value = r"H:\NRS528_2024\1_Class_Files\Classes\11_Toolboxes\Step_1_Data\Files_To_Make_Own_Toolbox_Tool\URI_Campus_Roads_OSM.shp" # This is a default value that can be over-ridden in the toolbox
params.append(input_line)

input_polygon = arcpy.Parameter(name="input_polygon",
                                displayName="Input Polygon",
                                datatype="DEFeatureClass",
                                parameterType="Required",  # Required|Optional|Derived
                                direction="Input",  # Input|Output
                                )
input_polygon.value = "YOUR INPUT POLY HERE" # This is a default value that can be over-ridden in the toolbox
params.append(input_polygon)

output = arcpy.Parameter(name="output",
                         displayName="Output",
                         datatype="DEFeatureClass",
                         parameterType="Required",  # Required|Optional|Derived
                         direction="Output",  # Input|Output
                         )
output.value = "YOUR OUTPUT DIR HERE" # This is a default value that can be over-ridden in the toolbox
params.append(output)
return params

# Code for execution function
input_line = parameters[0].valueAsText
input_polygon = parameters[1].valueAsText
output = parameters[2].valueAsText

arcpy.Clip_analysis(in_features=input_line,
                    clip_features=input_polygon,
                    out_feature_class=output,
                    cluster_tolerance="")


# This code block allows you to run your code in a test-mode within PyCharm, i.e. you do not have to open the tool in
# ArcMap. This works best for a "single tool" within the Toolbox.
def main():
    tool = NAME_OF_YOUR_TOOL() # i.e. what you have called your tool class: class Clippy(object):
    tool.execute(tool.getParameterInfo(), None)

if __name__ == '__main__':
    main()