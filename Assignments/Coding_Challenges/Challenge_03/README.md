# Coding Challenge 3

For this coding challenge, for each item below produce a Python file that executes addresses each task (total of 5 files  (3 py, 1 bat, 1 csv, in your repo):

### 1. Simple directory tree

Replicate this tree of directories and subdirectories:
```bash
├── draft_code
|   ├── pending
|   └── complete
├── includes
├── layouts
|   ├── default
|   └── post
|       └── posted
└── site
```

1. Using os.system or os.mkdirs replicate this simple directory tree.
2. Delete the directory tree without deleting your entire hard drive.

### 2. Push sys.argv to the limit

Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv, and does something to them. The rules:

1. Minimum of three arguments to be used.
2. You must do something simple in 15 lines or less within the Python file.
3. Print or file generated output should be produced.

### 3. Working with CSV

Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).

Using Python (csv) calculate the following:

1) Annual average for each year in the dataset.
2) Minimum, maximum and average for the entire dataset.
2) Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
3) Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
