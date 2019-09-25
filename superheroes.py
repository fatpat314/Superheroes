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

#Ability attack method
    def attack(self): #!!!!!!!!!!!!!!!! attack_strength
        attack_strength = random.randint(0,self.max_damage)
        return(attack_strength)
#Weapon Object
class Weapon(Ability):
    #weapon attack method
    def attack(self): #!!!!!!!!!!!! max_damage
        attack = random.randint(self.max_damage//2, self.max_damage)
        return attack

#armor object
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
#Block method
    def block(self):
        max_block = random.randint(0,self.max_block)
        return max_block

#Team Object
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    #adding a hero to the self.heroes list
    def add_hero(self, hero):
        self.heroes.append(hero)
        pass


    #Loop over heroes and print their names
    def view_all_heroes(self):
        for hero in self.heroes:
            print (hero.name)

    #remove hero from list
    def remove_hero(self, name):
        for hero in self.heroes:
            if name in hero.name:
                name_index = int(self.heroes.index(hero))
                self.heroes.pop(name_index)

        else:
            return 0

# Hero object
class Hero:
    def __init__(self, name, starting_health = 100,):
        self.abilities = []
        self.armors = []
        self.name = name
        self.current_health = starting_health
        self.starting_health = starting_health
# add an ability to hero
    def add_ability(self, ability):
         #self.ability = Ability
         self.abilities.append(ability)

# hero attack
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
#heros armor
    def add_armor(self,armor):
        self.armors.append(Armor(armor.name, armor.max_block))
#hero defend
    def defend(self, damage_amt):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked
#hero is hit
    def take_damage(self,damage):
        damage = damage - self.defend(damage)
        self.current_health -= damage

#checks if you are still alive
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
#The fight
    def fight(self, opponent):
        #while loop to run through undeturmened game (spelling is whatever)
        #if opponent and self have no ability "Its a Draw"
        while self.is_alive() and opponent.is_alive():
            if opponent.abilities and self.abilities == []:
                print("It's a draw")
                break

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            #if self health is less then or equal to 0 you lose. vice versa
            if self.current_health <= 0:
                print(f'{opponent.name} Wins!!')
            elif opponent.current_health <= 0:
                print(f'{self.name} Wins!!!')






#prints
if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    team1 = Team("test_team")
    team1.add_hero(hero1)
    #ability = Ability("Great Debugging", 50)
    #another_ability = Ability("Smarty Pants", 90)
    #hero = Hero("Grace Hopper", 200)
    #hero.take_damage(150)
    #print(hero.is_alive())
    #hero.take_damage(15000)
    #print(hero.is_alive())
    #hero.add_ability(ability)
    #hero.add_ability(another_ability)
    #shield = Armor("Shield", 50)
    #hero.add_armor(shield)
    #hero.take_damage(50)
    #print(hero.current_health)


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
