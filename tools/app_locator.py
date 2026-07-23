import os
from config import SEARCH_PATHS
import json 

def load_apps_path():
    try:
        with open("data/apps_path.json")as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}


def save_apps_path(paths):
    with open("data/apps_path.json","w") as file:
        json.dump(paths, file, indent=4)


def find_executable(exc_name):
    paths=load_apps_path()
    if exc_name in paths:
        return paths[exc_name]
    
    for search_path in SEARCH_PATHS:
        if not os.path.exists(search_path):
            continue

        for root,dirs,files in os.walk(search_path):
            for file in files:
                if file==exc_name:
                    full_path= os.path.join(root,file)
                    paths[exc_name]=full_path
                    save_apps_path(paths)
                    return full_path

    return None