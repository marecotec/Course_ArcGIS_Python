# Coding Challenge 9

In this coding challenge, your objective is to utilize the radiating lines code used in class "9_Cursors" to take an input of sites from a provided Shapefile (Site_Locations.zip), use the radiating lines code to calculate "fetch distances" for each 10 degree bearing in a manner that originated from [Davies & Johnson (2006)](https://www.sciencedirect.com/science/article/pii/S0272771406001867). Finally, clip the resulting fetch lines by the NB_Coastline.zip shapefile, and report the mean plus standard deviation of the fetch distance for each site: 9 sites, A1....C3 in meters. We don't have wind data so can't calculate the estimate as accurately as in Davies & Johnson (2006).


```python
origin_x, origin_y = (-71.42,  41.47)
distance = 1
angle = 10  # in degrees

OutputFeature = out_name

#create list of bearings
angles = range(0, 360,angle)


for ang in angles:
    angle = float(int(ang))
    (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
    (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
    (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)

    cur = arcpy.InsertCursor(OutputFeature)
    lineArray = arcpy.Array()

    start = arcpy.Point()
    (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
    lineArray.add(start)

    end = arcpy.Point()
    (end.ID, end.X, end.Y) = (2, end_x, end_y)
    lineArray.add(end)

    feat = cur.newRow()
    feat.shape = lineArray
    cur.insertRow(feat)

    lineArray.removeAll()
    del cur
```
