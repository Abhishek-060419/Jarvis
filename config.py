import os

APP_ALIASES = {
    # Browsers
    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",
    "edge": "msedge.exe",
    "microsoft edge": "msedge.exe",

    # Development
    "vs code": "Code.exe",
    "vscode": "Code.exe",
    "visual studio code": "Code.exe",

    # Terminal
    "command prompt": "cmd.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "windows terminal": "WindowsTerminal.exe",

    # File Management
    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",

    # Utilities
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "task manager": "Taskmgr.exe",

    # Office
    "word": "WINWORD.EXE",
    "microsoft word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "microsoft excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    "microsoft powerpoint":"POWERPNT.EXE",
    "ppt":"POWERPNT.EXE",


    # Media
    "spotify": "Spotify.exe"
}

SEARCH_PATHS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expanduser(r"~\AppData\Local\Programs"),
]