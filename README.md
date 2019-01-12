# ArcGIS automation through scripting with Python
### University of Rhode Island (Spring 2019)

![Banner Image](https://raw.githubusercontent.com/marecotec/Course_ArcGIS_Python/master/images/banner.png)

[[https://github.com/marecotec/Course_ArcGIS_Python/blob/master/images/banner.png|alt=octocat]]

**Course Description:** One of the most powerful elements of ArcGIS, beyond its vast visualization capabilities, is the ability to automate nearly all processing tasks using Python. Python is a popular programming language that is easy for beginners to understand but has vast capabilities through the addition of numerous third-party packages. ArcGIS itself uses an additional proprietary package known as arcpy, which extends Python with powerful geospatial capabilities, spatial file management and also allows us to process data with other libraries such as numpy and scipy. In this class, we will introduce you to Python and how it functions primarily within ArcGIS Desktop, but much should be applicable to ArcGIS Pro. We will develop scripts to automate and extend some common geoprocessing tasks and learn how we can build scripts into fully functioning toolboxes for dissemination. We will use Github for developing and sharing our code, so it is expected that everyone has a free account on that site, plus students can get private repositories for free. I am open to what problems we tackle, so do bring your ideas to class, and we can look at what data we process to capture the breadth of your varied interests. We will undertake several coding assignments, and these will form the basis for the final grade that is allocated.

**Pre-requisites:** Must have demonstrable proficiency using ArcGIS. For example, you must have completed an ArcGIS class prior to this course, or if you have not, then you must successfully complete my online “Intro to ArcGIS” course in advance of this class.

**Reading:** The University has free access to a great resource for this course, and in fact many of our examples are based upon this: “ArcPy and ArcGIS – Geospatial Analysis with Python” by Silas Toms. Click [here](https://uri-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=01URI_ALMA51174200860002396&context=L&vid=01URI&lang=en_US&search_scope=Books_More&adaptor=Local%20Search%20Engine&tab=default_tab&query=any,contains,ArcPy%20and%20ArcGIS%20–%20Geospatial%20Analysis%20with%20Python&sortby=rank&offset=0) to go to the book through the URI Library website.

```python
import arcpy

arcpy.AddMessage('Hello world')
```
