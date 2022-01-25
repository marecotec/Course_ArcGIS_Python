# Coding Challenge 9

In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic partitioning of your dataset. In this coding challenge, I want you to work with the Forest Health Works dataset from [RI GIS](https://www.rigis.org/datasets/ri-forest-health-works-project-points-all-invasives?geometry=-73.625%2C41.322%2C-69.307%2C42.040) (I have provided this as a downloadable ZIP file in this repository). 

Using the arcpy.da module (yes, there are other ways and better tools to do this), I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile, and do some basic counts of the dataset. In summary, please addressing the following:

1) Count how many individual records have photos, and how many do not (2 numbers), print the results.

2) Count how many unique species there are in the dataset, print the result.

3) Generate two shapefiles, one with photos and the other without.

