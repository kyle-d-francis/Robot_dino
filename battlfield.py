from robot import Robot
from dinosaur import Dinosaur
class battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        pass

    def display_welcome(self):
        welcome_message = input('welcome to the rice fields, would you like to start the battle?')
        if welcome_message == 'yes':
            return welcome_message

    def battle_phase(self):
        
        pass

    def display_winner(self):
        pass