# ArcGIS automation through scripting with Python
### University of Rhode Island (Spring 2019)

![Banner Image](/images/banner.png?raw=true)

**Course Description:** One of the most powerful elements of ArcGIS, beyond its vast visualization capabilities, is the ability to automate nearly all processing tasks using Python. Python is a popular programming language that is easy for beginners to understand but has an enormous range of capabilities through the addition of numerous third-party packages. ArcGIS itself uses an additional proprietary package known as arcpy, which extends Python with powerful geospatial capabilities, spatial file management and also allows us to process data with other libraries such as numpy and scipy. In this class, we will introduce you to Python and how it functions primarily within ArcGIS Desktop, but much should be applicable to ArcGIS Pro. We will develop scripts to automate and extend some common geoprocessing tasks and learn how we can build scripts into fully functioning toolboxes for dissemination. We will use Github for developing and sharing our code, so it is expected that everyone has a free account on that site, plus students can get private repositories for free. I am open to what problems we tackle, so do bring your ideas to class, and we can look at what data we process to capture the breadth of your varied interests. We will undertake several coding assignments, and these will form the basis for the final grade that is allocated.

**Pre-requisites:** Students should have a degree of proficiency using ArcGIS. For example, you must have completed an ArcGIS class prior to this course, or if you have not, then you should attempt my online [“Intro to ArcGIS”](https://learn.anddavies.co.uk/project/introduction-to-arcgis/) course in advance of this class.

**Reading:** The University of Rhode Island has free access to a great resource for this course, and in fact many of our examples are based upon this: “ArcPy and ArcGIS – Geospatial Analysis with Python” by Silas Toms. Click [here](https://uri-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=01URI_ALMA51174200860002396&context=L&vid=01URI&lang=en_US&search_scope=Books_More&adaptor=Local%20Search%20Engine&tab=default_tab&query=any,contains,ArcPy%20and%20ArcGIS%20–%20Geospatial%20Analysis%20with%20Python&sortby=rank&offset=0) to go to the book through the URI Library website.

```python
import arcpy
arcpy.AddWarning(r"It's not going to be easy, but..")
arcpy.AddMessage(r"Let's get started!")
```

### Course schedule


Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |	Topic
------------ | ---------
Jan 25 | **1. Introduction:** Overview of different assignments for this class. Set up Github accounts. **2. Interacting with Python:** The different Python environments and ways to interact with Python through ArcGIS (and not) – Python.exe, bat files, just clicking on a *.py, geoprocessing command line, PyCharm, toolboxes (*.pyt and traditional).
Feb 1 |	**3. Python basics:** Commenting, import statements for packages, variables and data types (str, int, float, lists, tuples, dictionaries). Iteration using: for loops, if/elif/else statements, while statements. Code cleanliness (indentation using tabs/spaces, spotting indentation errors), Using Functions to block code. Zero-based indexing.
Feb 8 | **4. Python modules:** Cover modules such as *os*, *sys*. Basic file and system manipulation.
Feb 15 | **5. Arcpy module:** Present basic arcpy functionality, where can you find scripts and information, cover basic functionality. Setting environments within arcpy.
Feb 22 |	**6. Building basic scripts:** Cover basic coding tasks, and introduce error handling, print statements and various messaging functionality.
Mar 1 |	**7. Building your first *big* script by cheating:** Using ModelBuilder and ArcToolbox to export python scripts. Extending exported python scripts.
Mar 8 | **8. File handling and input to arcpy:** How to interact with and code input for tools that are available through arcpy.
Mar 15 | *Spring break, no classes*
Mar 22 | **9. Functions:** Avoid repeating code using functions.
Mar 29 | **10. Cursors and Table Manipulation:** Selecting, searching, iterating through and updating tabular data.
Apr 5  | **11. Geometry objects:** Programmatically creating geometry objects, points, lines and polygons.
Apr 12 | **12. Raster manipulation:** Creating and working with raster datasets in arcpy.
Apr 19 | **13. Python Toolboxes:** Pythonizing your toolboxes to provide usable interactive toolbox scripts all within a single python file.
Apr 26 | **14. Designing scripts for others:** Building scripts that can be used by others, open source licenses to protect you and your code and dissemination through Github.
