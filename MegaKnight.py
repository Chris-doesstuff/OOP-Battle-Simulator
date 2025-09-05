from enemy import Enemy

class MegaKnight(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.attack_power = 40
        self.health = 420
    
    def attack(self):
        if self.health < 100:
            print(f"{self.name} is enraged! Attack power doubled!")
            self.attack_power = 80
        

        return self.attack_power
    
    
