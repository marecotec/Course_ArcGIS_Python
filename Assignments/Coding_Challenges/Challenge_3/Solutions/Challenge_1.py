# 1. Simple directory tree
#
# Replicate this tree of directories and subdirectories:
#
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

import os

# Create the directory where we will dump these folders
root_path = "D:\Empty_Dir"
os.mkdir(root_path)

# Now make folders
first_level = ["draft_code", "includes", "layouts", "site"]

for folder in first_level:
    # I am using os.path.join to join my folders
    os.mkdir(os.path.join(root_path, folder))

# Same again, for draft code folders
second_level = ["pending", "complete"]

for folder in second_level:
    # I am using os.path.join to join my folders
    os.mkdir(os.path.join(root_path, "draft_code", folder))

# different way for layouts
os.mkdir(os.path.join(root_path, "layouts", "default"))
os.mkdir(os.path.join(root_path, "layouts", "post"))
os.mkdir(os.path.join(root_path, "layouts", "post", "posted"))

# delete all folders, find by Googling "delete files and folders python"
import shutil
shutil.rmtree(root_path)

