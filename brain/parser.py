import string

INTENT={
    "OPEN_APP":["open","launch","start"],
    "CLOSE_APP":["close","terminate"],
    "SEARCH_WEB":[  "search for",
                    "search the web",
                    "search the web for",
                    "search online",
                    "search online for",

                    "google",
                    "google for",
                    "google search",
                    "google search for",

                    "look up",
                    "look this up",
                    "look it up",
                    "look for",

                    "find",
                    "find information",
                    "find information about",
                    "find information on",
                    "find out",
                    "find out about",
                    "find out what",

                    "look for information",
                    "look for information about",
                    "look for information on",

                    "search online for information",
                    "search the internet",
                    "search the internet for",
                    "search online for information about"],

    "PLAY_MUSIC":["play"],
    "STOP_MUSIC":["stop","pause"],
    "GET_TIME":["time"],
    "GET_DATE":["date"],
    "SHUTDOWN_PC":["shutdown"],
    "RESTART_PC":["restart","reboot"],
    "SLEEP_PC":["sleep"],
    "LOCK_PC":["lock"],
    "WEATHER":["weather"],
    "EXIT_ASSISTANT":["exit","goodbye","quit"]
}

NORMALIZATION = {
    "turn off": "shutdown",
    "power off": "shutdown"
}

def normalize(text):
    for phrase, replacement in NORMALIZATION.items():
        text=text.replace(phrase,replacement)
    return text

def parse(text):
    text=text.lower()
    text=normalize(text)
    #remove all punctuations
    text = text.translate(str.maketrans("", #replace nothing
                                         "", #with nothing
                                           string.punctuation))#delete punctuations
    words=text.split()  #array of words

    for intent, keywords in INTENT.items():
        for keyword in keywords:
            if keyword in words:
                indx=words.index(keyword)
                parameter=" ".join(words[indx+1:])
                if parameter=="":
                    parameter=None

                return{
                    "intent":intent,
                    "parameter":parameter
                }
            
    
    return{
        "intent":None,
        "parameter":None
    }