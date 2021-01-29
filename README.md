# Geographical Information Systems in Python
### University of Rhode Island (Spring 2020)

![Banner Image](/images/banner.png?raw=true)

**Course Description:** One of the most powerful elements of ArcGIS, beyond its vast visualization capabilities, is the ability to automate nearly all processing tasks using Python. Python is a popular programming language, at its core, it is easy for beginners to understand. However, it also has vast capabilities, largely through the addition of numerous third-party packages. ArcGIS itself uses an additional proprietary package known as arcpy, which extends Python with powerful geospatial capabilities, spatial file management and also allows us to process data with other libraries such as numpy and scipy. In this class, we will introduce you to Python and how it functions primarily within ArcGIS Desktop, but much will be applicable to ArcGIS Pro and other open source programs such as QGIS. This is a skills-based course, so we will begin by learning basic-programming skills using the Python language. We will advance these within the arcpy environment and begin developing basic scripts to automate and extend some common geoprocessing tasks. We will develop an understanding of good coding practice, open source programming and turn scripts into fully functioning toolboxes for wider dissemination to non-programming geospatial analysts. We will base our learning around Github and use this for developing and sharing our code.

**Pre-requisites:** Students should have a degree of proficiency using ArcGIS, usually obtained through successful completion of NRS 410. If you have not, then you should contact me, to refresh your skills, you can always take my online [“Intro to ArcGIS”](https://learn.anddavies.co.uk/project/introduction-to-arcgis/) course in advance of this class.

**Course credit:** This is a three-credit course, that includes weekly self-study learning components, lectures, computer-based hands on classes and assignments to work towards these credits (see below in the Assessment section and the Schedule).

**Course goals:**
*	Expose you to the Python programming language and provide opportunity to practice using basic functionality.
*	Introduce arcpy and how this can be used to automate and extend geoprocessing tasks.
*	Provide you with the skills needed to successfully develop Python tools that can be used, not only by yourself, by other users.
*	Provide practice in the use of Github as a tool for code dissemination and storage.

**Learning outcomes:**
*	**LO-1** You will be able to produce basic Python code that is functional and extendable: 1) including operating system operations, including file creation, manipulation, searching and filtering. 2) Core Python functionality including for loops, if/else, lists and variable manipulation. 3) Extending the capabilities of Python by importing various libraries.
*	**LO-2** You will be able to undertake basic geoprocessing tasks by using Python code and the arcpy library, that mirror routines that you would previously have used the graphical user interface or ModelBuilder to complete.
*	**LO-3** You will be able to package code into usable Python Toolboxes that will be available to users via ArcToolbox, which will include adequate help and explanatory files for other users to execute your Toolbox.
*	**LO-4** You will be able to participate in the open source software movement including the practices of code sharing and dissemination through the Github website. You will be able to produce understandable code that is appropriately commented to allow other users to run your programs.

**Self-learning component:** Each week prior to meeting in the computer teaching laboratory, you will undertake self-study exercises to address simple coding problems in preparation for the class. These are called “Coding Challenges” and are a type of flipped classroom whereby you undertake self-learning prior to coming to class where we undertake more advanced topics. These challenges are designed to be achievable in approximately two to three hours and must be completed prior to the specific class for which they are assigned (see Schedule), as they are assessed by quizzes whereby you will answer questions pertaining to either coding practice or outputs from each challenge (see Assessment below). Some challenges will require additional preparation including research on code-repositories such as textbooks, Github, or forums such as Stack Overflow. Your code from each challenge must be maintained in your Github account, as it forms part of your overall coding portfolio.

**Classroom component:** In class, we will explore basic programming concepts and advanced geospatial applications that are suited for automation using Python. During lab, we will work on training materials produced by the instructor, which are designed to ensure you meet the learning outcomes of the course. We will use the software development program PyCharm, which allows rapid code generation and can be linked into ArcGIS for code execution.

**Reading resources:**
*	“ArcPy and ArcGIS”, 2017, 2nd Edition by Silas Toms and Dara O’Beirne, freely available through the URI Library. I do not expect you to purchase this unless you want a reference text.
*	Additional material for certain lectures will be posted on Github or listed in the description of each lecture.

```python
import arcpy
arcpy.AddWarning(r"It's not going to be easy, but..")
arcpy.AddMessage(r"Let's get started!")
```

### Course schedule

Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Topic | Assignments |
------------ | ------------ | ------------ |
Week 1 | Introduction, overview of different assignments for this class and modes of teaching. Set up Github accounts. The different Python environments and ways to interact with Python through ArcGIS (and not) – Python.exe, bat files, just clicking on a *.py, geoprocessing command line, PyCharm, toolboxes (*.pyt and traditional). | |
Week 2 | Introduction to Python basics. Commenting, import statements for packages, variables and data types (str, int, float, lists, tuples, dictionaries). Iteration using for loops, if/elif/else statements, while statements. Code cleanliness (indentation using tabs/spaces, spotting indentation errors), Using Functions to block code. Zero-based indexing. | Coding challenge 1 |
Week 3 | Introduction to Python modules.os, sys. Basic file and system manipulation. arcpy. Present some arcpy functionality, where can you find scripts, basic resources. | Coding challenge 2 |
Week 4 |Introduction to Python modules.os, sys. Basic file and system manipulation. arcpy. Present some arcpy functionality, where can you find scripts, basic resources. | Coding challenge 3 |
Week 5 |Building basic scripts. Cover basic coding tasks, and introduce error handling, print statements and various messaging functionality. | Coding challenge 4 |
Week 6 | Building your first script by cheating. Using ModelBuilder and ArcToolbox to export python scripts. Extending exported python scripts. | Coding challenge 5 |
Week 7 | Environments, functions and file handling. Setting environments within arcpy. How to interact with and code input for tools that are available through arcpy. Avoid repeating code using functions. | Mid-term Assignment Set |
Week 8 | Introduction to Cursors. Selecting, searching, updating data using arcpy functions, and non-arcpy alternatives. | Coding challenge 6 |
Week 9 | Geometry objects and raster manipulation. Creating geometry objects, points, lines and polygons. Creating and working with raster datasets. | Coding challenge 7 |
Week 10 | Spatial analyst and other extensions in Python. Practice using various ArcGIS extensions through arcpy. Check out/in licenses, advanced functionality. | Coding challenge 8 |
Week 11 | Interacting with ArcGIS Desktop from code. Techniques to manipulate the desktop environment. | Coding challenge 9 |
Week 12 | Effective Python Toolboxes. Pythonizing your toolboxes to provide usable interactive scripts all within a single python file. | Coding challenge 10 |
Week 13 | Designing scripts for others. Building scripts that can be used by others, open source licenses to protect you and your code and dissemination through Github. | |
