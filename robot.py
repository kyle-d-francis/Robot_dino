from weapon import Weapon 
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name ) :
        self.name = name 
        self.health = 100
        self.active_weapon = Weapon('battle axe',20)

    def attack_dinosaur(self, dinosaur):
        #dinosaurs health subtracted by attack power of robots weapon
        dinosaur.health -= self.active_weapon.attack_power 
        print(f'{ dinosaur.name} has been struck by a battle axe, he has {dinosaur.health} remaining.')
        if dinosaur.health == 0:
            print(f'{dinosaur.name} has been killed')


    


