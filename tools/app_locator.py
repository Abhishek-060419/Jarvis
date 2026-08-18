import os
import json
import shutil

from config import SEARCH_PATHS


def load_apps_path():
    try:
        with open("data/apps_path.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}


def save_apps_path(paths):
    with open("data/apps_path.json", "w") as file:
        json.dump(paths, file, indent=4)


def find_executable(exe_name):
    paths = load_apps_path()


    if exe_name in paths:
        cached_path = paths[exe_name]

        if os.path.exists(cached_path):
            print("Found in cache.")
            return cached_path

  
        print("Cached path is invalid. Removing entry.")
        del paths[exe_name]
        save_apps_path(paths)

    system_path = shutil.which(exe_name) #search directories and return the path variable

    if system_path:
        print("Found in system PATH.")
        paths[exe_name] = system_path
        save_apps_path(paths)
        return system_path

    for search_path in SEARCH_PATHS:

        if not os.path.exists(search_path):
            continue

        for root, dirs, files in os.walk(search_path):

            if exe_name in files:
                full_path = os.path.join(root, exe_name)

                print("Found by directory search.")

                paths[exe_name] = full_path
                save_apps_path(paths)

                return full_path

    return None