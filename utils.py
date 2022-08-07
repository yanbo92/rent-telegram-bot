import os
import json
from typing import Dict


def read_json(file_path) -> Dict:
    if not os.path.exists(file_path):
        raise Exception("{} non-existent".format(file_path))
    with open(file_path, 'r', encoding="utf-8") as f:
        file_info = json.load(f)
    return file_info
