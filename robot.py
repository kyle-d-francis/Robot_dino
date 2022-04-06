from weapon import Weapon 
class Robot:
    def __init__(self, name ) :
        self.name = name 
        self.health = 100
        self.active_weapon = Weapon('battle axe',20)

    def attack_dinosaur(self,dinosaur):
        #dinosaurs health subtracted by attack power of robots weapon
        self.health = 100
        self.active_weapon.attack_power = 15
        self.health = self.health - self.active_weapon.attack_power 
        print(f'{ self.name} has been struck by a battle axe, he has {self.health} remaining.')
        if dinosaur.health == 0:
            print(f'{self.name} has been killed')


    


