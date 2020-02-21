# Coding Challenge 5

For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this time obtain your own input data, and I want you to generate heatmaps for **TWO** species.

You can obtain species data from a vast array of different sources, for example:

* [obis](https://www.obis.org) - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long strings that don't fit the Shapefile specification.
* [GBIF](https://www.gbif.org)
* [Maybe something on RI GIS](http://www.rigis.org)
* Or just *Google* species distribution data

My requirements are:
1. The two input species data must be in a **SINGLE** CSV file, you must process the input data to separate out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading the species data from the same source so the columns match.
2. Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you provide the species data along with your Python code.
3. The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
4. You leave no trace of execution, except the resulting heatmap files.
5. You provide print statements that explain what the code is doing, e.g. Fishnet file generated.
