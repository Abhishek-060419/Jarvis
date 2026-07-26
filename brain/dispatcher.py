from actions.open_apps import open_application

def dispatch(command):
    intent = command["intent"]
    parameter = command["parameter"]

    if intent == "OPEN_APP":
        if parameter:
            open_application(parameter)
        else:
            print("❌ No application specified.")

    else:
        print(f"⚠️ Intent '{intent}' not implemented yet.")