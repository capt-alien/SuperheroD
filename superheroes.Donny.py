import random
"""This project recived plenty of help from Eric Botcher, all code simularities are
    intentional with express permission to use. Hi Anisha!!"""

def validator(valid_entries, input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            for item in valid_entries:
                if item == entry:
                    is_valid = True
                else:
                    pass
            if is_valid:
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")

def validator_num(input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            if entry.isdigit()== True:
                is_valid = True
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")


class Hero:
    def __init__(self, name, health = 100):
        self.abilities = []
        self.name = name
        self.armors = []
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        """runs through all abilities and creates an attack attack value"""
        total_attacks = 0
        for ability in self.abilities:
            total_attacks += ability.attack()
            print(total_attacks)
        return total_attacks

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.defense
        return int(total_defense)



class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        attack_value = random.randint((self.attack_strength // 2), self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        # Update the value of the current attack strength with the # new value passed in as a parameter.
        self.attack_strength = attack_strength


class Weapon(Ability):
    def attack(self):
        weapon_attack_value = random.randint(0, self.attack_strength)
        return weapon_attack_value


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.num_kills = 0

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        if len(self.heroes) <= 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0

    def find_hero(self, name):
        if len(self.heroes) <= 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        totalTeamAttackStrengths = 0
        for hero in self.heroes:
                team_attack_strengths += hero.attack()
                print("Total Team Attack Strength: {}".format(team_attack_strengths))
        num_kills = other_team.defend(team_attack_strengths)
        for hero in self.heroes:
            if num_kills >= 1:
                hero.kills += 1
        return(num_kills)

    def defend(self, damage_amt):
        totalTeamDefense = 0
        excessDamage = 0
        for hero in self.heroes:
            for armor in hero.armors:
                totalTeamDefense += armor.defense

        for hero in self.heroes:
            for ability in hero.abilities:
                damage_amt += ability.attack_strength
        excessDamage = damage_amt - totalTeamDefense
        return self.deal_damage(excessDamage)

    def deal_damage(self, damage):
        divisionOfDamage = damage // len(self.heroes)
        numHerosDiedInAttack = 0
        for hero in self.heroes:
            if hero.health > 0:
                hero.health -= divisionOfDamage
                if hero.health <= 0:
                    numHerosDiedInAttack += 1
                    hero.deaths += 1
        return numHerosDiedInAttack

    def revive_heroes(self):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        print(self.name)
        for hero in self.heroes:
            print("{} had a kill/death ratio of {}/{}".format(hero.name, hero.kills, hero.deaths))

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena(Hero, Team):
    def __init__(self):
        """
        Declare variables
        """

    def build_abilities_list(self):
        # Return an ability and append ability
        abilities = [
            "Alien Attack",
            "Science",
            "Star Power",
            "Immortality",
            "Grandmas Cookies",
            "Blinding Strength",
            "Cute Kittens",
            "Team Morale",
            "Luck",
            "Captain Rainbow's death stare",
            "Obsequious Destruction",
            "The Kraken",
            "The Fire of A Million Suns",
            "Team Spirit",
            "Canada"]
        index = random.randint(0, len(abilities) - 1)
        ability_name = abilities[index]
        abil_att_Strength = random.randint(0, 600)
        one_ability = Ability(ability_name, abil_att_Strength)
        return one_ability

    def build_armors_list(self):
        armors = [
            "Calculator",
            "Laser Shield",
            "Invisibility",
            "SFPD Strike Force",
            "Social Workers",
            "Face Paint",
            "Damaskus Shield",
            "Bamboo Wall",
            "Forced Projection",
            "Thick Fog",
            "Wall of Will",
            "Wall of Walls",
            "Obamacare",
            "Thick Goo"]
        # Get one armor out of the list
        index = random.randint(0, len(armors) - 1)
        armor_name = armors[index]
        defense = random.randint(0, 600)
        one_armor = Armor(armor_name, defense)
        return one_armor

    def create_hero(self):
        heroes = [
            "Athena",
            "Jodie Foster",
            "Wonder Woman",
            "Christina Aguilera",
            "Gamora",
            "Supergirl",
            "Batgirl",
            "Carmen Sandiego",
            "Okoye",
            "America Chavez",
            "Cat Woman",
            "White Canary",
            "Nakia",
            "Mera",
            "Quake",
            "Wasp",
            "Storm",
            "Black Widow",
            "Ted Kennedy",
            "San Francisco",
            "Bananas"]
        index = random.randint(0, len(heroes) - 1)
        hero_name = heroes[index]
        hero = Hero(hero_name)
        # Ask how many abilities does the hero have then build that many abilities
        abilites_number = int(validator_num("How many abilities do you want your hero {} to have? ".format(hero.name)))
        for _ in range(0, abilites_number):
            ability = self.build_abilities_list()
            hero.add_ability(ability)
        print(hero.abilities)
        # Ask How many armor
        armors_number = int(validator_num("How many picecs of armor do you want your hero {} to have? ".format(hero.name)))
        # However many armor the user wants the hero get the ability and add to the heros list of armor that many times
        for _ in range(0, armors_number):
            hero.add_armor(self.build_armors_list())
        print(hero.armors)
        return hero

    def build_team_one(self):

        print("Welcome to the Killing Ground:")
        team_name = input("Name your team! ")

        self.team_one = Team(team_name)
        choosing_Team_Size = True
        while choosing_Team_Size:
            hero_number = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want to add a hero? (Y/N)")
            if hero_number == "Yes" or hero_number == "yes" or hero_number == "y" or hero_number == "Y":
                self.team_one.add_hero(self.create_hero())
                print(self.team_one.heroes)
            else:
                choosing_Team_Size = False

    def build_team_two(self):
        print("\n")
        print("Build Team 2!")
        team_name = input("Name your team Human!")
        self.team_two = Team(team_name)
        choosing_Team2_Size = True
        while choosing_Team2_Size:
            hero_number = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want to add a hero? (Y/N)")
            if hero_number == "Yes" or hero_number ==  "yes" or hero_number == "y" or hero_number == "Y" :
                self.team_two.add_hero(self.create_hero())
                print(self.team_two.heroes)
            else:
                choosing_Team2_Size = False


    def team_battle(self):
        """
        This method should continue to battle teams until one or both teams are dead.
        """
        print("\n")
        print("{} vs. {}".format(self.team_one.name, self.team_two.name))
        in_battle = True

        while in_battle:
             if self.team_one.attack(self.team_two) == len(self.team_two.heroes):
                 print("Team 1 Wins!!")
                 in_battle = False
             else:
                if self.team_two.attack(self.team_one) == len(self.team_one.heroes):
                    print("Team 2 Wins!!")
                    in_battle = False
                else:
                    continue

    def show_stats(self):
        """
        This method should print out the battle statistics including each heroes kill/death ratio.
        """
        self.team_one.stats()
        self.team_two.stats()

def main():
    # created a variable and assigned a boolean value
    game_is_running = True
    # Instantiate Game Arena - Object
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    # while condition is true run this code
    while game_is_running:
        arena.team_battle()
        arena.show_stats()


if __name__ == "__main__":
    main()
