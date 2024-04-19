
#####
# Step 1 - "Traditional" ArcToolboxes
#####

# In this process, we will create a "Script Tool" which will create a toolbox that we can interact with using the
# script below. This is a Walk Through Session, so follow as I go along.

# First you should add the Toolbox that I provided in Step_1_Data.zip, and we will look at the script and
# code used to initialize it. It needs a bit of work to get this running.

# 1. Add Toolbox provided to the Toolboxes pane.
# 2. Navigate to the script tool.
# 3. If we run this tool as is, we will get an error as the path to the tool will not be set correctly.
# 4. Right click the tool and select properties, update the file path to the script that I have provided: Testing_Tool_Script.py
# 5. Now run the tool.

# Now let's create our own. The script is provided below, and a brief description of the workflow is provided.

# 1. Open the Toolboxes pane in ArcGIS Pro, right click Add Toolbox, click new Toolbox icon in window that pops up, call it "Testing Toolbox.tbx"
# 2. Inside this new Toolbox, right click, Add "Script", then add the following params:
##### Name = TestTool1 - This is the machine name of the script
##### Label = Test Tool 1 - This shows up in ArcToolbox as the name of the tool.
##### Description = "Testing a tool, does nothing really".
##### Leave the rest as it is.
# 3. Click Next, now browse to select the "Script File", you will note that I have provided one for you in
# Step_1_Data.zip, called Testing_Tool_Script.py.
# 4. Click Next, here you add the individual parameters, we are going to add two inputs, first with a display name of "Input 1" in the
# top most box, on the left, and a datatype of "String", leave the parameter settings as their defaults. Second, "Input 2", and again
# datatype of "String"
# 5. Click finish! Test it by adding two different strings to the tool.


# Task - Taking the more complex code below, I want you to turn this into a toolbox. Note that it accepts
# three arguments, one input line file and one input polygon file, and an output file. You do not need to
# change the code below, just put it in its own Python file, and then create the appropriate parameters
# inside the toolbox settings as we just walked through.


# import arcpy
# # import sys
# #
# # input_line = sys.argv[1]
# # input_polygon = sys.argv[2]
# # output = sys.argv[3]
# #
# # arcpy.Clip_analysis(in_features=input_line,
# #                     clip_features=input_polygon,
# #                     out_feature_class=output,
# #                     cluster_tolerance="")