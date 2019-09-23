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
        attack_strength = random.randint(0,self.max_damage)
        print(attack_strength)

#armon method
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        max_block = random.randint(0,self.max_block)
        print(max_block)

class Hero:
    def __init__(self, name, starting_health = 100,):
        self.abilities = []
        self.armors = []
        self.name = name
        self.current_health = starting_health
        self.starting_health = starting_health

    def add_ability(self, ability):
         #self.ability = Ability
         self.abilities.append(ability)


    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage = ability.attack()
            return total_damage

    def add_armor(self,armor):
        self.armors.append()

    def defend(self, damage_amt):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked




#prints
if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())


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