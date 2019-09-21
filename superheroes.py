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

#attack method
    def attack(self):
        attack_strength = random.randint(0,20)
        print(attack_strength)

#armon method
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        max_block = random.randint(0,20)
        print(max_block)

class Hero:
    def __init__(self, name,current_health, abilities, starting_health = 100,):
        self.abilities = []
        self.armors = []
        self.name = name
        self.current_health = current_health
        self.starting_health = starting_health

    def add_ability(self, ability):
         self.ability = Ability
         self.abilities.append(ability)
         self.abilities.append(ability)




#prints
if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200,[])
    hero.add_ability(ability)
    print(hero.abilities)

    #print(my_hero.name)
    #print(my_hero.current_health)



    #ability = Ability("Debugging Ability", 20)
    #print(ability.name)
    #print(ability.attack())
    #print("------------------------------------------------")

    #armor = Armor("Armor", 20)
    #print(armor.name)
    #print(armor.block())
    #print("------------------------------------------------")
