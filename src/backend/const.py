import os
import sys
from datetime import datetime

CURRENT_PATH: str = os.path.abspath(os.path.dirname(sys.argv[0])).replace("\\", "/")
"""Absolute path to the execution folder.
NOTE: Running this path from another directory (other than main.py) may cause unexpected behavior."""
SOURCE_FOLDER: str = f"{CURRENT_PATH}/src"
"Source folder path. (./src)"
LOGGER_FOLDER_PATH: str = f"{CURRENT_PATH}/log"
"Logger folder path. (./log)"
LOGGER_FILE: str = (
    f"{LOGGER_FOLDER_PATH}/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
)
"Logger file. (./log/**)"
