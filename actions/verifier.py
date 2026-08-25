import requests
import json

#we are communicating with the llama server running on our computer via port 8080
Server_URL="http://127.0.0.1:8080"


Valid_Intents={ "OPEN_APP", 
               "CLOSE_APP", 
               "SEARCH_WEB", 
               "PLAY_MUSIC", 
               "STOP_MUSIC", 
               "GET_TIME", 
               "GET_DATE", 
               "SHUTDOWN_PC", 
               "RESTART_PC", 
               "SLEEP_PC", 
               "LOCK_PC", 
               "WEATHER", 
               "EXIT_ASSISTANT", 
               }

#we want the Qwen model to striclty adhere to these valid intents
System_Prompt = """You are the AI command verifier for Jarvis.

Your job is to verify or correct the parser's interpretation of a user command.

Rules:
1. Use ONLY the valid intents listed below.
2. NEVER create, rename, or invent an intent.
3. Determine the user's intended action or actions.
4. A user command may contain multiple actions.
5. Preserve the order of actions when order matters.
6. Identify dependencies between actions when necessary.
7. Do not consider capitalization or minor formatting differences to be corrections.
8. If the parser is correct, return CORRECT.
9. If the parser is wrong, return CORRECTED.
10. If the command cannot be understood with confidence, return AMBIGUOUS.
11. Return ONLY valid JSON.
12. Do not include explanations, reasoning, markdown, or extra text.

Valid intents:
OPEN_APP
CLOSE_APP
SEARCH_WEB
PLAY_MUSIC
STOP_MUSIC
GET_TIME
GET_DATE
SHUTDOWN_PC
RESTART_PC
SLEEP_PC
LOCK_PC
WEATHER
EXIT_ASSISTANT

Action dependency rules:
13. Every action has an index based on its position in the actions list.
14. Action indexing starts from 0.
15. The first action has index 0, the second action has index 1, the third action has index 2, and so on.
16. The "depends_on" field must contain either null or the index of another action.
17. Use "depends_on": null when an action does not depend on another action.
18. If an action depends on a previous action, set "depends_on" to that action's index.
19. The number in "depends_on" refers to the action's position, NOT to an intent.
20. Do not use an intent name such as "OPEN_APP" as the value of "depends_on".
21. Use "CORRECT" when the parser's interpretation already represents the user's intended action or actions.
22. Use "CORRECTED" when you change the parser's intent, parameter, or action plan.
23. Use "AMBIGUOUS" when the user's intended action cannot be determined with sufficient confidence.
24. If the status is AMBIGUOUS, return an empty actions list.
25. If the status is AMBIGUOUS, do not invent or guess an intent or parameter.

Example:
If the user says:
"Open Chrome and search for NASA news."

The correct action plan is:

{
    "status": "CORRECTED",
    "actions": [
        {
            "intent": "OPEN_APP",
            "parameter": "Chrome",
            "depends_on": null
        },
        {
            "intent": "SEARCH_WEB",
            "parameter": "NASA news",
            "depends_on": 0
        }
    ]
}

Here:
- Action 0 is OPEN_APP.
- Action 1 is SEARCH_WEB.
- Action 1 depends on Action 0.
- The value 0 refers to the first action, not to OPEN_APP itself.

Required output format:
{
    "status": "CORRECT",
    "actions": [
        {
            "intent": "VALID_INTENT",
            "parameter": "value",
            "depends_on": null
        }
    ]
}
"""
def verify(command,parsed_intent,parsed_parameter):
    #We create a prompt using the original user command the interpretation produced by our parser
    user_prompt=f"""User command:
        "{command}"

        Parser interpretation:
        intent={parsed_intent}
        parameter="{parsed_parameter}"
       """
    #data contains the system rules and the user prompt that will be sent to the Qwen modle throught the llama server
    data={
        "model": "Qwen/Qwen3-4B-GGUF:Q4_K_M",
        "messages":[
            {

        
            "role":"system",
            "content":System_Prompt
            },
            {
                "role":"user",
                "content":user_prompt
            }
        ]
    }

    #Send the system rules and the user prompt to the Qwen model using the  llama server 
    response=requests.post(
        f"{Server_URL}/v1/chat/completions",
        json=data
    )

    #conver the json result into python dictionary
    result=response.json()


    #obtain only the Qwen's actual response from the larger response
    content=result["choices"][0]["message"]["content"]

    #convert Qwen's JSON response from a string into a python dictionary
    verified=json.loads(content)

    #check if the status in response message is among what we explicitly asked
    status=verified.get("status")
    if status not in {"CORRECT","CORRECTED","AMBIGUOUS"}:
        return None 

    #check whether the response is in correct format as provided in system rules
    actions=verified.get("actions")
    if not isinstance(actions,list):
        return None 

    
    
    for index,action in enumerate(actions):

        #check whether each entry in actions is a dictionary
        if not isinstance(action,dict):
            return None

        #check whether each intent is strcitly within what we provided in system rules
        intent=action.get("intent")
        if intent not in Valid_Intents:
            return None 

        #check whether the parameter is null
        parameter=action.get("parameter")
        if parameter is None:
            return None

        #check whether the current action depends on any other action given in actions or if depends_on is out of bounds or if
        #depends on itself
        depends_on=action.get("depends_on")
        if depends_on is not None and not isinstance(depends_on,int):
            return None
        if depends_on is not None and (depends_on<0 or depends_on>=len(actions)):
            return None

        if depends_on==index:
            return None

        if status=="CORRECT":
            if len(actions)!=1:
                return None
            if intent!=parsed_intent:
                return None
            if parameter.lower()!=str(parsed_parameter).lower():
                return None



    return verified
        
