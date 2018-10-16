import random

def validator (list_of_valid_entries, input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            for item in list_of_valid_entries:
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

def validator_num (input_text):
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

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
        # Initialize starting values

    def attack(self):
        max_attack = self.attack_strength
        min_attack = max_attack //2
        attack = random.randint(min_attack, max_attack)
        return attack
         # Calculate lowest attack value as an integer.
         # Use random.randint(a, b) to select a random attack value.
         # Return attack value between 0 and the full attack.

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
        # Update attack value

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
        """Instantiate name and defense strength."""

    def defend(self):
        return random.randint(0, self.defense)
        """
        Return a random value between 0 and the
        initialized defend strength.
        """


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.weapons = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
        # Initialize starting values

    def add_ability(self, ability):
        self.abilities.append(ability)
        # abilities.append = ##no idea what to put here
        # Add ability to abilities list

    def add_armor(self,armor):
        self.armors.append(Armor)
        ##add_armor to pass pytest

    def add_weapon(self,weapon):
        self.weapons.append(weapon)
        ##weapon add to hero

    def attack(self):
        total_attack = 0
        for item in self.abilities:
            total_attack += item.attack()
        return total_attack
        # Run attack() on every ability hero has


    def defend(self):
        total_defence = 0
        for armor in self.armors:
            total_defence += armor.defend()
        if self.health ==0:
            total_defence == 0
        return total_defence
        """
        This method should run the defend method on each piece of armor
         and calculate the total defense. If the hero's health is 0, the hero
          is out of play and should return 0 defense points.
        """


    def take_damage(self, damage_amt):
        num_kills = 0
        self.health = self.health - damage_amt
        if self.health <= 0:
            # self.health = 0
            num_kills += 1
        """
        This method should subtract the damage amount from the
        hero's health.
        If the hero dies update number of deaths.
        """

    def add_kill(self, num_kills):
        self.kills += num_kills
        """
        This method should add the number of kills to self.kills
        """

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        weapon_attack_value = random.randint(0, self.attack_strength)
        return weapon_attack_value

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        """Instantiate resources."""


    def add_hero(self, Hero):
        self.heroes.append(Hero)
        """Add Hero object to heroes list."""


    def remove_hero(self, name):
        for i, o in enumerate(self.heroes):
            if o.name == name:
                self.heroes.pop(i)
        return 0
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """

    def find_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                return hero
        return 0
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

    def view_all_heroes(self):
        for Hero in self.heroes:
            print(Hero.name)
        """Print out all heroes to the console."""


    def attack(self, other_team):
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()
        other_team_defence = other_team.defend(total_attack)
        for hero in self.heroes:
            hero.add_kill(other_team_defence)
        """
        This method should total our teams attack strength and call the
         defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """

    def defend(self, damage_amt):
        team_defence = 0
        excess_damage = 0
        for hero in self.heroes:
            team_defence += hero.defend()
        excess_damage += damage_amt - team_defence
        if excess_damage >= 0:
            return self.deal_damage(excess_damage)
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be
        evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """

    def deal_damage(self, damage):
        total_dammage = damage//len(self.heroes)
        total_deaths = 0
        for hero in self.heroes:
            hero.take_damage(total_dammage)
            if hero.health < 0:
                total_deaths += 1
        return total_deaths
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        for hero in self.heroes:
            print(hero.name, " : ", hero.kills/hero.deaths, " kills to deaths")
        """
        This method should print the ratio of kills/deaths for
         each member of the team to the screen.
        This data must be output to the terminal.
        """

    def update_kills(self):
        for hero in self.heroes:
            hero.kills += total_deaths
        return hero.kills
        """
        This method should update each hero when there is a team kill.
        """

class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = None
        self.team_two = None
        self.hero_list = []

    def create_abilities(self, hero):
        name = input("What is the ability name? ")
        attack_strength = random.randint(45, 5000)
        ability = Ability(name, attack_strength)
        hero.add_ability(ability)
        #return Ability(name, attack_strength)

    def create_armor(self, hero):
        name = input("What is the name of the Armor? ")
        defence_bonus = random.randint(0,5000)
        armor = Armor(name, defence_bonus)

    def create_weapon(self, hero):
        name = input("Name Your Weapon! ")
        weapon_attack_value = random.randint(0,5000)


    def create_heroes(self):
        name = input("Please enter Name of SuperHero: ")
        start_health = validator_num("Enter Starting Health ")
        hero = Hero(name, start_health)
        self.hero_list.append(hero)
        print(self.hero_list[0].name)
       #create and Add ability
        num_of_abilities = int(validator_num("How many abilities does this hero have? "))
        for _ in range(0, num_of_abilities):
            self.create_abilities(hero)
            #Create and add armor
        pices_armor = int(validator_num("How many pices of Armor does this hero have? "))
        for _ in range(0, pices_armor):
            self.create_armor(hero)
            hero.add_armor(pices_armor)
            #Creates and adds weapon
        w_prompt = validator(["Yes","yes","y", "No", "no", "n"],"Would you like to give this hero a weapon? ")
        if w_prompt == "Yes" or "yes" or "y":
            hero.add_weapon(self.create_weapon(hero))
        else:
            pass



    def build_team(self, team):
        team = []
        team_name = input("What is the name of your team? ")
        team = Team(team_name)
        print("team {}".format(team))

        cont_hero = True
        while cont_hero:
            prompt1 = validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add a hero? ")
            if prompt1 == "Yes" or "yes" or "y":
                for hero in self.hero_list:
                    print(hero.name)
                hero1 = input("Please enter Name of SuperHero: ")
                self.find_hero(hero1)
                self.add_hero(hero1)

            else:
                cont_hero = False
                print(team_name,": ", team)

    def build_team_one(self):
        self.build_team(self.team_one)
        # team_name = build_team()


    def build_team_two(self):
        self.build_team(self.team_two)

    def team_battle(self):
        battling = True
        while battling:
            team_one.attack(team_two)
            team_two.defend(team_one)
            team_one.deal_damage(team_two)
            if team_two.total_deaths == len(team_two):
                print(team_one.team_name + "wins! ")
                battling = False
            else:
                team_two.attack(team_one)
                team_one.defend(team_two)
                team_two.deal_damage(team_one)
                if team_one.total_deaths == len(team_one):
                    print(team_two.team_name + "wins! ")
                    battling =False

    def show_stats(self):
        team_one.stats
        team_two.stats

## start of the program
print("Welcome to the Proving Ground:")
print("   Where two teams enter, and only one team leaves")
#number_of_heroes = validator(int,"How many champions would you like to have?")
number_of_heroes = int(validator_num("How many Champions would you like? "))
for _ in range(0, number_of_heroes):
    Arena().create_heroes()
print

Arena().build_team_one()
Arena().build_team_two()
