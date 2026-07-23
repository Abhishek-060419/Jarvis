import os
from config import SEARCH_PATHS

folder=r"D:\Python\Jarvis"

for root,dirs,files in os.walk(folder):
    print("Current folder:",root)
    print("Subfolders:",dirs)
    print("Files:",files)
    print("-"*40)