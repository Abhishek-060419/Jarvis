import subprocess
from config import APP_ALIASES
from tools.app_locator import find_executable

#returns the path of an executable application or None if not found
def find_application_path(app_name):
    exe_name=APP_ALIASES.get(app_name.lower())
    if exe_name is None:
        return None
    return find_executable(exe_name)

def open_application(app_name):
    print(f"1.Recived application name {app_name}")
    path=find_application_path(app_name)
    print(f"2.Found path {path}")

    if path is None:
        print(f"Unknown Application: {app_name}")
        return False

    print(f"3.Launching app")

    #use a new process to open the application
    try:
        process = subprocess.Popen(path)
        print("4: Process started. PID =", process.pid)
        return True
    except Exception as e:
        print("ERROR:", e)
        return False