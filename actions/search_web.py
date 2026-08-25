import webbrowser
from urllib.parse import quote
import subprocess

def search_web(query,browser_path=None):
    if not query:
        return False
    
    formatted_query=quote(query)
    base_url="http://www.google.com/search?q="
    url=base_url+formatted_query

    print(url)

    if browser_path:
        try:
            subprocess.Popen([browser_path,url])
            return True
        except Exception:
            return False


    return webbrowser.open(url)
