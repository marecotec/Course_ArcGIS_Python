
#####
# Step 2 - Python Toolboxes
#####

# The process to create a "Traditional" toolbox takes you out of Python, and somewhat can limit what you can
# do. The solution is an all Python Toolbox, a hidden gem of python and arcpy. There is a lot of information
# about them here; http://desktop.arcgis.com/en/arcmap/10.3/analyze/creating-tools/a-quick-tour-of-python-toolboxes.htm

# The template for a Python toolbox uses classes and functions. See a class as a higher level function that allows
# us to keep code separate. Below is an example template, I shall walk you through the different parts:

# Note:
### class Toolbox defines the toolbox, you only have this once, but you can have multiple tool classes, i.e.
### Tool, Tool1, Tool2 etc, just extend the self.tools = [Tool, Tool1, Tool2] and add the corresponding
### classes for the new tools.


import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

# I have created a rudimentary Python Toolbox for you in Step_2_Data/Python_Toolbox_Example, add this to ArcToolbox