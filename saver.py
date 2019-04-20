import json
import os
from pathlib import Path
import shutil

SAVER_DIR = Path(__file__).resolve().parent / "save"
SAVER_DIR.mkdir(parents=True, exist_ok=True)


def saver(func):
    filename = SAVER_DIR / (func.__name__ + ".save")

    def save_data(*args, **kwargs):
        if os.path.exists(filename):
            with open(filename) as fin:
                data = json.load(fin)
                return data
        print(f"Executing {func.__name__}")
        data = func(*args, **kwargs)
        with open(filename, 'w') as fout:
            json.dump(data, fout)
        return data
    return save_data


def clear():
    shutil.rmtree(SAVER_DIR)
    SAVER_DIR.mkdir(parents=True, exist_ok=True)
