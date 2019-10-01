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
    def attack(self):
        attack_strength = random.randint(0,self.max_damage)
        return(attack_strength)
#Weapon Object
class Weapon(Ability):
    #weapon attack method
    def attack(self):
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

    def attack(self, other_team):
        #Randomly select a living hero from each team to fight
        #until one team wins
        rm_hero = random.shuffle(self.heroes)
        rm_opp = random.shuffle(other_team.heroes)


        for hero in self.heroes:
            for opponent in other_team.heroes:
                while self.rm_hero.is_alive() and self.rm_opp.is_alive():
                    self.rm_hero.fight(self.rm_opp)

        #Might need to change some things on page 5

        if hero.is_alive():
                print(f'Team {self.name} is victorious!!!')
        else:
            print(f'Team {other_team.name} is victorious!!!')

    def revive_heroes(self, health=100):
        #Revives all heroes health to original value
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.

        for hero in self.heroes:
            #print (f'{hero.name}:'(hero.kills/hero.deaths))

            print("Hero: " + hero.name + " | Kills: " + str(hero.kills) + " | Deaths: " + str(hero.deaths))

class Arena:
    def __init__(self):
        self.team_one = Team("Team one")
        self.team_two = Team("Team two")

    def create_ability(self):
        name = input("Name your ability: ")
        max_damage = input("Set the maximum damage for your ability: ")
        return Ability(name, max_damage) #might need to make max_damage an int

    def create_weapon(self):
        name = input("Name your a weapon: ")
        max_damage = input("Set the maximum damage for your weapon: ")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Name your Armor: ")
        max_block = input("Set the maximum strength of your armor: ")
        return Armor(name, max_block)

    def create_hero(self):
        name = input("Enter your heroes name: ")
        hero = Hero(name)

        armor = input("Would you like armor? (Y/N)")
        if armor == "y":
            armor = self.create_armor()
            hero.add_armor(armor)
        else:
             pass

        weapon = input("Would you like a weapon? (Y/N)")
        if weapon == "y":
            weapon = self.create_weapon()
            hero.add_weapon(weapon)
        else:
            pass

        ability = input("Would you like an ability? (Y/N)")
        if ability == "y":
            ability = self.create_ability()
            hero.add_ability(ability)
        else:
            pass
        return hero
        #Arena.team_one.append(hero)

    def build_team_one(self):
        team_one_name = input("Name your first team: ")
        number_of_heroes = int(input("Enter a number for the amount of heroes you would like in your first team: "))
        for i in range(0, int(number_of_heroes)):
            #print(i)
            hero = self.create_hero()
            print(hero.name)
            self.team_one.add_hero(hero)

        #print(f'Print heros {self.team_one.heroes[0]}')

    def build_team_two(self):
        team_two_name = input("Name your second team: ")
        number_of_heroes2 = input("Enter a number for the amount of heroes you would like in your second team: ")
        for i in range(0, int(number_of_heroes2)):
            hero = self.create_hero()
            print(hero.name)
            self.team_one.add_hero(hero)

    def team_battle(self):

        self.winning_team = self.build_team_one.attack(self.build_team_two)
        #print(self.team_one.name)
        #print(self.team_one.heroes[0])
        #print(self.team_one.heroes[0].name)
        #self.team_one.attack(self.team_two)



    def show_stats(self):

        print("The winners are: " + self.winning_team)

        self.build_team_one.stats()
        self.build_team_two.stats()

        if self.winning_team == self.build_team_one.name:
            for hero in self.build_team_one.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)
        elif self.winning_team == self.build_team_two.name:
            for hero in self.build_team_two.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)


        #print("Team ones kill/death ratio is: {}".format(self.team_one.stats()))
        #print("Team twos kill/death ratio is: {}".format(self.team_two.stats()))

        #winner: if opponent hero list is = 0 ....?
        #if Team.team_two(self.heroes) == 0 and Team.team_one(self.heroes) > 0:
            #print("{} WINS!!!".format(self.team_one_name))
        #else:
            #pass
#
        #if Team.team_one(self.heroes) == 0 and Team.team_two(self.heroes) > 0:
            #print("{}WINS!!!".format(self.team_two_name))


# Hero object
class Hero:
    def __init__(self, name, starting_health = 100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.current_health = starting_health
        self.starting_health = starting_health
        self.kills = 0
        self.deaths = 0

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
        #self.armors.append(Armor(armor.name, armor.max_block))
        self.armors.append(armor)

#adding heros armor
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

#hero defend
    def defend(self):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked

#hero is hit
    def take_damage(self, damage):
        damage = damage - self.defend()
        self.current_health -= damage

#checks if you are still alive
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

#The fight
    def fight(self, opponent):
        #while loop to run through undeturmened game
        #if opponent and self have no ability "Its a Draw"
        while self.is_alive() and opponent.is_alive():
            if opponent.abilities and self.abilities == []:
                print("Evenly Matched! ")
                break

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            #if self health is less then or equal to 0 you lose. vice versa
            #if self dies opponets adds 1 to add_kill and self adds to self.add_death
            if self.current_health <= 0 or self.abilities == []:
                opponent.add_kill(1)
                self.add_death(1)
                print(f'{opponent.name} won!')


            elif opponent.current_health <= 0 or opponent.abilities == []:
                # elif opponent dies add 1 to self.add_kill
                # and one to opponent.add_death
                self.add_kill(1)
                opponent.add_death(1)
                print(f'{self.name} won!')


    def add_kill(self,num_kills):
            #this should add the number of kills to self.kills
            # if game ends and self.current_health is not 0 you self.kill
            self.kills += num_kills

    def add_death(self, num_deaths):
        #this should add numbers of deaths to self.death
            self.deaths += num_deaths





#prints
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
    #hero1 = Hero("Wonder Woman")
    #hero2 = Hero("Dumbledore")               #creat heroes
    #ability1 = Ability("Super Speed", 300)
    #ability2 = Ability("Super Eyes", 130)
    #ability3 = Ability("Wizard Wand", 80)
    #ability4 = Ability("Wizard Beard", 20)
    #hero1.add_ability(ability1)
    #hero1.add_ability(ability2)
    #hero2.add_ability(ability3)
    #hero2.add_ability(ability4)
    #hero1.fight(hero2)
    #team1 = Team("test_team")
    #team2 = Team("test_team2")
    #team1.add_hero(hero1)
    #team2.add_hero(hero2)
    #team1.fight(team2)
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
