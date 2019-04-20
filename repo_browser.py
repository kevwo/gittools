import os
import os.path
from saver import saver


@saver
def find_components(subdirectory=None):
    if subdirectory is None:
        subdirectory = "."
    directories = []
    for dirpath, dirnames, filenames in os.walk(subdirectory):
        if "INFO" in filenames:
            directories.append(f"{dirpath}")
    return directories
