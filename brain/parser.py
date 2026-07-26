import string

INTENT={
    "OPEN_APP":["open","launch","start"],
    "CLOSE_APP":["close","terminate"],
    "SEARCH_WEB":["search","find","google"],
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
    text = text.translate(str.maketrans("", "", string.punctuation))
    words=text.split()  

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