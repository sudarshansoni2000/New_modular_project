import os , sys  #OS module provide way to interact with operating system # sys module provide access to system -specific parameters and func..It is often used for tasks like cmd . Basically it is essential for task like command like scripting
from pathlib import Path   # provide way to work with file system paths "Path" is central component of path lib 
import logging 

while True:
    project_name=input("Enter Your Project Name: ")
    if project_name != "":
        break

# src/__init__.py
# src/components/__init__.py

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"config/config.yaml",
    "schema.py",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]


for filepth in list_of_files:
    filepath=Path(filepth)
    filedir , filename =os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir , exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        logging.info("File is already present at: {filepath}")


