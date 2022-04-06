from robot import Robot
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 100
    
    def attack_robot(self, robot):
        #robots health subtracted by dinosaurs attack power
        Dinosaur.health -= self.attack_power
        print(f'{self.name}''has been hit by an attack')
        if self.health == 0:
            print(f'{self.name}has been killed')