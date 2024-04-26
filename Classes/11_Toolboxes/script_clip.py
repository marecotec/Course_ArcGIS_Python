
import arcpy
import sys

input_line = sys.argv[1]
input_polygon = sys.argv[2]
output = sys.argv[3]

arcpy.Clip_analysis(in_features=input_line,
                     clip_features=input_polygon,
                     out_feature_class=output,
                     cluster_tolerance="")