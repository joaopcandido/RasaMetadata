# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json


# Função criada para extrair o metadata da última mensagem do usuário
def extract_metadada_from_last_user_event(tracker):
     events = tracker.current_state()['events']
     user_events = []
     for e in events:
         if e['event'] == 'user':
             user_events.append(e)
     return user_events[-1]['metadata']


# Action criada para teste de manipulação do Metadata
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Hello World!")
         metadata = extract_metadada_from_last_user_event(tracker)['metadata']
         metadata = metadata.replace("'", "\"")
         dict_metadata = json.loads(metadata)
         print(dict_metadata.keys())

         return []
