# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import random
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence

class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"
     

    def computer_choice(self):
        generatednum = random.randint(1,3)

        if generatednum == 1:
            computerchoice = "pedra"
        elif generatednum == 2:
            computerchoice = "papel"
        elif generatednum == 3:
            computerchoice = "tesoura"
        
        return(computerchoice)
    
    def format_user_choice(self, user_choice):

        user_choice = user_choice.lower()
        
        if user_choice == "r":
            user_choice = "pedra"
        elif user_choice == "p":
            user_choice = "papel"
        elif user_choice == "s":
            user_choice = "tesoura"
        
        return(user_choice)

    def check_winner(self, user_choice, comp_choice):

        user_choice = user_choice.lower()
        
        if user_choice == "pedra" and comp_choice == "tesoura":
            winner = "jogador"
        elif user_choice == "pedra" and comp_choice == "papel":
            winner = "computador"
        elif user_choice == "papel" and comp_choice == "pedra":
            winner = "jogador"
        elif user_choice == "papel" and comp_choice == "tesoura":
            winner = "computador"
        elif user_choice == "tesoura" and comp_choice == "papel":
            winner = "jogador"
        elif user_choice == "tesoura" and comp_choice == "pedra":
            winner = "computador"
        else:
            winner = "empate"
        
        return(winner)
    

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Jogar pedra papel tesoura
        user_choice = self.format_user_choice(tracker.get_slot("game_choice")) + ''
        comp_choice = self.computer_choice()

        dispatcher.utter_message(text=f"Você escolheu {user_choice} e o computador escolheu {comp_choice}.")


        winner = self.check_winner(user_choice, comp_choice)

        if winner == "jogador":
            dispatcher.utter_message(text="Parabéns, você ganhou!")
        elif winner == "computador":
            dispatcher.utter_message(text="O computador ganhou esse round.")
        else:
            dispatcher.utter_message(text="É um empate!")


        return []


class ActionRandomDog(Action):

    def name(self) -> Text:
        return "action_random_dog"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        # The API endpoint
        url = "https://dog.ceo/api/breeds/image/random"
    
        # A GET request to the API
        response = requests.get(url)

        # Get picture url
        response_json = response.json()
        image = '"'+response_json['message']+'"'

        dispatcher.utter_message(image=image)


        return []