from weapon import Weapon 

class Robot:
    def __init__(self, name ) :
        self.name = name 
        self.health = 100
        self.active_weapon = Weapon('battle axe',20)

    def attack(self, dinosaur):
        #dinosaurs health subtracted by attack power of robots weapon
        dinosaur.health -= self.active_weapon.attack_power 
        print(f'')
        pass

