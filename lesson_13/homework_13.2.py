import os
import pathlib
import json
import logging

logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s",
                    filename='json_korotenko.log', force=True)
logger = logging.getLogger(__name__)

current_dir = pathlib.Path().absolute()

# get the list of json files to check
files = []
for path_ in current_dir.iterdir():
    if path_.is_dir() and path_.name == "work_with_json":
        files = [elem.name for elem in path_.iterdir() if elem.is_file()]

# validate format of the json files
for file in files:
    file_path = os.path.join(current_dir, "work_with_json", file)
    print(file)
    with open(file_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            logging.error(e)
