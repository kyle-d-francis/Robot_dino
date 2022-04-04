from robot import Robot
from dinosaur import Dinosaur
class battlefield:
    def __init__(self):
        self.robot = Robot('Gyspy Danger')
        self.dinosaur = Dinosaur('Dan',15)

    def run_game(self):
        pass

    def display_welcome(self):
        welcome_message = input('welcome to the rice fields, would you like to start the battle?')
        while welcome_message != "yes":
            next_message = input( 'are you sure you dont want to start the mayhem?')
        if welcome_message == 'yes':
            return welcome_message

    def battle_phase(self):
        while 

        pass

    def display_winner(self):
        pass