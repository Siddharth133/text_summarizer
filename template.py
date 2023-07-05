import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "NLP_Project"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for files_path in list_of_files:
    files_path = Path(files_path)
    filedir, filename = os.path.split(files_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory {filedir} for the file {filename}")

    if (not os.path.exists(files_path)) or (os.path.getsize(files_path)):
        with open(files_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {files_path}")

    else:
        logging.info(f"{filename} is already exist")
