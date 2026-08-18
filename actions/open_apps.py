import subprocess
from config import APP_ALIASES
from tools.app_locator import find_executable


def open_application(app_name):
    print(f"1.Recived application name {app_name}")
    exe_name=APP_ALIASES.get(app_name.lower())
    print(f"2.Exec name {exe_name}")

    if exe_name is None:
        print(f"Unknown Application: {app_name}")
        return False

    path=find_executable(exe_name)
    print(f"3.found path {path}")

    if path is None:
        print("Path not found!")
        return False

    print(f"4.Launching app")

    #use a new process to open the application
    try:
        process = subprocess.Popen(path)
        print("Step 5: Process started. PID =", process.pid)
        return True
    except Exception as e:
        print("ERROR:", e)
        return False