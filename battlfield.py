from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__(self):
        self.robot = Robot('Gyspy Danger')
        self.dinosaur = Dinosaur('Dan',15)

    def run_game(self):
        #welcome message
        self.display_welcome()
        #robot attacks
        #dino attacks
        self.battle_phase()
        #display winner
        self.display_winner()
    
         

    def display_welcome(self):
        self.welcome = print( 'welcome to the rice fields, lets start the battle.')
    
        

    def battle_phase(self):
        Dinosaur.attack_robot(self, Robot)
        Robot.attack_dinosaur(self, Dinosaur)
    



    

    def display_winner(self):
        pass

    
