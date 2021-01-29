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
*	“ArcPy and ArcGIS”, 2017, 2nd Edition by Silas Toms and Dara O’Beirne, freely available through the URI Library.
*	Additional material for certain lectures will be posted on Github or listed in the description of each lecture.

```python
import arcpy
arcpy.AddWarning(r"It's not going to be easy, but..")
arcpy.AddMessage(r"Let's get started!")
```

### Course schedule

Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Topic | Assignments |
------------ | ------------ | ------------ |
Week 1 | **Lecture:** Introduction, overview of different assignments for this class and modes of teaching. **Laboratory:** Set up Github accounts. The different Python environments and ways to interact with Python through ArcGIS (and not) – Python.exe, bat files, just clicking on a *.py, geoprocessing command line, PyCharm, toolboxes (*.pyt and traditional). | |
Week 2 | **Lecture:** Introduction to Python basics. **Laboratory:** Commenting, import statements for packages, variables and data types (str, int, float, lists, tuples, dictionaries). Iteration using for loops, if/elif/else statements, while statements. Code cleanliness (indentation using tabs/spaces, spotting indentation errors), Using Functions to block code. Zero-based indexing. | Coding challenge 1 |
Week 3 | **Lecture:** Introduction to Python modules. **Laboratory:** os, sys. Basic file and system manipulation. arcpy. Present some arcpy functionality, where can you find scripts, basic resources. | Coding challenge 2 |
Week 4 | **Lecture:** Introduction to Python modules. **Laboratory:** os, sys. Basic file and system manipulation. arcpy. Present some arcpy functionality, where can you find scripts, basic resources. | Coding challenge 3 |
Week 5 | **Lecture:** Building basic scripts. **Laboratory:** Cover basic coding tasks, and introduce error handling, print statements and various messaging functionality. | Coding challenge 4 |
Week 6 | **Lecture:** Building your first script by cheating. **Laboratory:** Using ModelBuilder and ArcToolbox to export python scripts. Extending exported python scripts. | Coding challenge 5 |
Week 7 | **Lecture:** Environments, functions and file handling. **Laboratory:** Setting environments within arcpy. How to interact with and code input for tools that are available through arcpy. Avoid repeating code using functions. | Mid-term Assignment Set |
Week 8 | Spring Break - No Classes |  |
Week 9 | **Lecture:** Introduction to Cursors. **Laboratory:** Selecting, searching, updating data using arcpy functions, and non-arcpy alternatives. | Coding challenge 6 |
Week 10 | **Lecture:** Geometry objects and raster manipulation. **Laboratory:** Creating geometry objects, points, lines and polygons. Creating and working with raster datasets. | Coding challenge 7 |
Week 11 | **Lecture:** Spatial analyst and other extensions in Python. **Laboratory:** Practice using various ArcGIS extensions through arcpy. Check out/in licenses, advanced functionality. | Coding challenge 8 |
Week 12 | **Lecture:** Interacting with ArcGIS Desktop from code. **Laboratory:** Techniques to manipulate the desktop environment. | Coding challenge 9 |
Week 13 | **Lecture:** Effective Python Toolboxes. **Laboratory:** Pythonizing your toolboxes to provide usable interactive scripts all within a single python file. | Coding challenge 10 |
Week 14 | **Lecture:** Designing scripts for others. **Laboratory:** Building scripts that can be used by others, open source licenses to protect you and your code and dissemination through Github. |  |

**Additional information:**

**Grade Scale:** A = 94.0–100%; A- = 90.0–93.9%; B+ = 87.5–89.9%; B = 84.0–87.4%; B- = 80.0–83.9%; C+ = 77.5–79.9%; C = 74.0–77.4%; C- = 70.0–73.9%; D+ = 67.5–69.9%; D = 60.0–67.4%; F = below 59.9%

**Special Needs:** We strive to be fully inclusive in the development of course materials and teaching. If you have as requirement for any special accommodation with respect to the curriculum, instruction, or assessments please inform the instructor, and provide the instructor with documentation from URI in the first few weeks of the semester.

**Religious Observance and University Sanctioned Events:** As per the University Policy on Religious Observance and University Sanctioned Events, if you do not attend class or lab due to their observance of religious holy days or University Sanctioned Events, you will not be penalized for missing class. However, you are responsible for informing the instructor in advance that you will be missing class and you are responsible for making up any missed work.

**Academic Honesty:** Students are expected to be honest in all academic work. A student’s name on any written work, quiz or exam shall be regarded as assurance that the work is the result of the student’s own independent thought and study. Work should be stated in the student’s own words, properly attributed to its source.  Students have an obligation to know how to quote, paraphrase, summarize, cite and reference the work of others with integrity. The following are examples of academic dishonesty.
*	Using material, directly or paraphrasing, from published sources (print or electronic) without appropriate citation
*	Claiming disproportionate credit for work not done independently
*	Unauthorized possession or access to exams
*	Unauthorized communication during exams
*	Unauthorized use of another’s work or preparing work for another student
*	Taking an exam for another student
*	Altering or attempting to alter grades
*	The use of notes or electronic devices to gain an unauthorized advantage during exams
*	Fabricating or falsifying facts, data or references
*	Facilitating or aiding another’s academic dishonesty
*	Submitting the same paper for more than one course without prior approval from the instructors.

**Late Work:** Due dates (in the syllabus) have been designed to provide you with a clear workplan for this course so that you cannot leave everything to the last minute; you must take a regular approach to handing in work and building your portfolios. Work submitted after this time for each deadline, but no more than 5 days late will have 50% grade reduction and feedback will be provided. Work submitted more than 5 but less than 10 days late will receive 0%, but feedback will be provided. Work that is 10 days late will not be accepted. If you think you have a valid excuse for handing in work late, please contact the instructor to discuss any issues.

**Attendance, participation and illness:** Attendance is critical to your success in this class. To earn full credit, you must attend and participate in each and every lecture and laboratory. If you have an emergency, or you are ill, you are expected to contact the instructor in advance of class. This particularly pertains to flu-like symptoms, so if you do exhibit signs of flu, contact the instructor and stay home to minimize transference of the virus. Unexcused absences will result in a lower course grade. According to university policy, documented medical illnesses, emergencies, observance of religious holidays or participation in university-sanctioned athletics or other events are the only valid excuses for missing classes and deadlines, but the instructor must be informed in advance. Any missed work is the student’s responsibility and you should contact the instructor in advance to discuss this.
