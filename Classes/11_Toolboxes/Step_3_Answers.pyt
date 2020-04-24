import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Clippy"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Clippy]


class Clippy(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clippy Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Line",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_line.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Roads_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_line)
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        input_polygon.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\URI_Campus_Buildings_OSM.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_polygon)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\Course_ArcGIS_Python\Classes\11_Toolboxes\Step_2_Data\Output.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
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
        input_line = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=input_line,
                            clip_features=input_polygon,
                            out_feature_class=output,
                            cluster_tolerance="")
        return

# This code block allows you to run your code in a test-mode within PyCharm, i.e. you do not have to open the tool in
# ArcMap. This works best for a "single tool" within the Toolbox.
def main():
    tool = Clippy()
    tool.execute(tool.getParameterInfo(), None)

if __name__ == '__main__':
    main()