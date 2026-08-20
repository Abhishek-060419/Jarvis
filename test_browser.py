import webbrowser
from urllib.parse import quote

#webbrowser.open('https://www.google.com')
query= "how does tcp work ?"
print(quote(query))

phrases = [
    "search",
    "search for",
    "search the web",
    "search the web for"
]

print(sorted(phrases,key=len,reverse=True))