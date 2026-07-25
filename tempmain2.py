from tools.app_locator import find_executable

apps = [
    "chrome.exe",
    "Code.exe",
    "Spotify.exe",
    "calc.exe",
    "notepad.exe",
    "cmd.exe"
]

for app in apps:
    print(f"\nSearching for: {app}")
    path = find_executable(app)
    print(f"Result: {path}")