import subprocess
from config import APP_ALIASES
from tools.app_locator import find_executable


def open_applications(app_name):
    exe_name=APP_ALIASES.get(app_name.lower())

    if exe_name is None:
        print(f"Unknown Application: {app_name}")
        return 

    path=find_executable(exe_name)

    if path is None:
        print("Path not found!")
        return 

    subprocess.Popen(path)