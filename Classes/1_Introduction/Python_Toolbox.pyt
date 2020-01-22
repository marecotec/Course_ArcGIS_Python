import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Test Toolbox"
        self.alias = ""
        self.tools = [test_tool]


class test_tool(object):
    def __init__(self):
        self.label = "Test Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []

        # Input 1 - Just a string
        input1 = arcpy.Parameter(name="input1",
                                          displayName="Please enter a name:",
                                          datatype="GPString",
                                          parameterType="Required",
                                          direction="Input",
                                          )
        params.append(input1)
        return params

    def isLicensed(self):
        return True

    def execute(self, parameters, messages):

        input1 = parameters[0].valueAsText

        arcpy.AddMessage("Hey " + input1 + " this is a message!")
        arcpy.AddWarning("Hey " + input1 + " this is a warning!")

        return