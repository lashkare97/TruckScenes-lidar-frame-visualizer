import os
import json

def load_json(path, name):
    """Loads a JSON file given the directory path and filename."""
    with open(os.path.join(path, f"{name}.json"), 'r') as f:
        return json.load(f)
