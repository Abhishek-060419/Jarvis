import webbrowser
from urllib.parse import quote

def search_web(query):
    if not query:
        return False
    
    formatted_query=quote(query)
    base_url="http://www.google.com/search?q="
    url=base_url+formatted_query

    print(url)
    return webbrowser.open(url)
