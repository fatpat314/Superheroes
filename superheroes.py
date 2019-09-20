#superhero.py
import random

class Ability:
    def __init__ (self, name, attack_strength):
        '''Create Instance Veriables:
            name:String
            max_damage: Integer
        '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        attack_strength = random.randint(0,20)
        print(attack_strength)

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
