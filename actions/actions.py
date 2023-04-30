# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import random
import requests

from dict import countries as countries_file

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

country = {}
correct_op = ''

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
        user_choice = self.format_user_choice(tracker.get_slot("rps_choice")) + ''
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


class ActionPlayCapitals(Action):

    def name(self) -> Text:
        return "action_play_cotw"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        # Choose four countries and one of them to figure out the answer
        countries = countries_file.countries
        size = len(countries)

        num_list = list(range(0,size))
        options = random.sample(num_list, k = 4)
        chosed_index = random.choice(options)

        global country 
        country = countries[chosed_index]


        # Generate question message and get the correct answer
        message = f"Esse país é localizado na {country['continent']}. "
        message += f"Qual é a capital de {country['name']}?\n"

        global correct_op
        letters = ['A','B','C','D']
        
        for i, op in enumerate(options):
            country_op = countries[op]
            message += '\n' + str(letters[i]) + ' - ' + str(country_op['capital'])

            if country_op['name'] == country['name']:
                correct_op = str(letters[i])
        

        dispatcher.utter_message(text=message)
            

        return []


class ActionCapitalsValidateAnswer(Action):

    def name(self) -> Text:
        return "action_validate_cotw_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        # Get the choosed option 
        user_choice = str(tracker.get_slot("cotw_choice"))
        user_choice = user_choice.upper()

        if correct_op == user_choice:
            dispatcher.utter_message(text='Correto!')
        else:
            incorrect_m = 'Incorreto, a resposta correta é ' + correct_op + ' - ' + country['capital'] + '.'
            dispatcher.utter_message(text=incorrect_m)


        return []