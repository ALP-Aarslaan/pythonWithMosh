from pathlib import Path

"""
there are two types of paths:
1. absolute paths
    c:\machine learning\ML
2. Relative paths
"""
path = Path("a1")
print(path.exists())

path = Path("ecommerce")
print(path.exists())

path = Path("Emails")
# path.mkdir() this is used to make directory in out Python project
path = Path("Emails")
# path.rmdir() # this is used for deleting a directory
path = Path()
for files in path.glob("*.py"):
    print(files)

path = Path()
for files in path.glob("*"):
    print(files)