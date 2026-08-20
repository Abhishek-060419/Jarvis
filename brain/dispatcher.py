from actions.open_apps import open_application
from voice.speak import speak
from actions.search_web import search_web

def dispatch(command):
    intent = command["intent"]
    parameter = command["parameter"]

    if intent == "OPEN_APP":
        if parameter:
            speak(f"Opening {parameter}.")  
            success=open_application(parameter)

            if not success:
                speak(f"Sorry boss, I couldn't find an application called {parameter}.")

            return True
        
        else:
            print("❌ No application specified.")
            return True

    elif intent == "SEARCH_WEB":
        speak("Searching web")
        success=search_web(parameter)

        if not success:
            speak("Sorry boss, I couldn't find the search results from web")
        return True

    elif intent=="EXIT_ASSISTANT":
        speak("Okay boss. Goodbye")
        return False

    else:
        speak("Sorry boss, I didn't understand that command.")
        return True