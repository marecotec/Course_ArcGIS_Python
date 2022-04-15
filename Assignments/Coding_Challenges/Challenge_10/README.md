# Coding Challenge 10

Our coding challenge this week follows from the last exercise that we did in class during Week 6 and improve our practice with rasters from Week 10.

Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI.

Before you start, here is a suggested workflow:

1) Extract the Step_3_data.zip file into a known location.
2) For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis) https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first calculation.

The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your code submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for an area of RI that you find interesting.
