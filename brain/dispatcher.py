from actions.open_apps import open_application
from voice.speak import speak

def dispatch(command):
    intent = command["intent"]
    parameter = command["parameter"]

    if intent == "OPEN_APP":
        if parameter:
            speak(f"Opening {parameter}.")
            open_application(parameter)
            return True
        else:
            print("❌ No application specified.")
            return True

    elif intent=="EXIT_ASSISTANT":
        speak("Okay boss. Goodbye")
        return False

    else:
        print(f"⚠️ Intent '{intent}' not implemented yet.")
        return True