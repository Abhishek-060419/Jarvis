from actions.open_apps import open_application,find_application_path
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

def dispatch_actions(actions):

    #actions is the list from the verified json from verifier.py

    for index,action in enumerate(actions):

        intent=action["intent"]
        parameter=action["parameter"]
        depends_on=action["depends_on"]

        if intent=="SEARCH_WEB" and depends_on is not None:

            dependency=actions[depends_on]
            if dependency["intent"]!="OPEN_APP":
                return False
            
            browser_name=dependency["parameter"]
            browser_path=find_application_path(browser_name)

            if browser_path is None:
                speak(f"Sorry boss, I was not able to  find an application called {browser_name}.")
                return True
            
            success=search_web(parameter,browser_path)
            if not success:
                speak("Sorry boss,  I couldn't perform the search and happy onam")

            
        else:
            if intent=="OPEN_APP":
                skip=False

            #check whether any later actions depends_on open app so that redudant opening can be avoided
                for other_action in actions:
                    if(other_action["intent"]=="SEARCH_WEB" and other_action["depends_on"]==index):
                        skip=True
                        break
                print("OPEN_APP skip =", skip)
                if skip:
                    continue

            running=dispatch(action)

            if not running:
                return False

    return True