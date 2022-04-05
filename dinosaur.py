class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack_robot(self, robot):
        #robots health subtracted by dinosaurs attack power
        robot.health -= self.attack_power
        print(f'{robot.name}''has been hit by an attack')
        if robot.health == 0:
            print(f'{robot.name}has been killed')