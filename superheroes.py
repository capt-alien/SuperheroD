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
        abiliities_list = []
        weapon_list = []
        armor_list = []
        hero_list = []

    def create_abiliities(self, name, attack_strength):
        return superheroes.Ability(name, attack_strength)
        ability.name = input("What is the ability name?")
        ability.attack_strength = random.randint(45, 5000)
        ability.name.apend(abiliities_list)

    def create_armor(self, name, defence_bonus):
        armor.name = input("What is the name of the Armor? ")
        armor.defence_bonus = random.randit(0,5000)
        armor.name.append(armor_list)

    def create_weapon(self, name, weapon_attack_value):
        weapon.name = input("Name Your Weapon!")
        weapon.weapon_attack_value = random.randit(0,5000)
        weapons.name.append(weapon_list)



    def create_heroes(self, name, start_health):
        name = input("Please enter Name of SuperHero: ")
        start_health = input("Enter Starting Health")
       #create and Add ability
        num_of_abilities = input("How many abilities does this hero have?"):
        for _ in range(0, num_of_abilities):
            self.create_ability()
            self.add_ability()
            #Create and add armor
        pices_armor = input("How many pices of Armor does this hero have?"):
                for _ in range(0, pices_armor):
                    self.create_armor()
                    self.add_armor(pices_armor)
            #Creates and adds weapon
        w_prompt = validator(["Yes","yes","y", "No", "no", "n"],"Would you like to give this hero a weapon?")
        if w_prompt == "Yes" or "yes" or "y":
            self.add_weapon(create_weapon())



    def build_team(self, team):
        team = []
        team_name = input("What is the name of your team? ")
        team = Team(team_name)

        cont_hero = True
        while cont_hero:
            prompt1 = validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add a hero? ")
            if prompt1 == "Yes" or "yes" or "y":
                team.view_all_heroes()
                hero1 = input("Please enter Name of SuperHero: ")
                find_hero = hero1
                Team.add_hero(hero1)

                # cont_ability = True
                # while cont_ability:
                #     prompt2 = validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add an ability? ")
                #     if prompt2 == "Yes" or "yes" or "y":
                #         ability1 = input("Please enter ability name: ")
                #         add_ability(hero1, ability1)
                #     elif prompt2 == "No" or "no" or "n":
                #         cont_ability = False
                #
                # cont_weapon = True
                # while cont_ability:
                #     prompt2 = validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add a Weapon? ")
                #     if prompt2 == "Yes" or "yes" or "y":
                #         weapon1 = input("Please enter weapon name: ")
                #         add_weapon(hero1, weapon1)
                #     elif prompt2 == "No" or "no" or "n":
                #         cont_ability = False
                #
                # cont_armor = True
                # while cont_armor:
                #     prompt2 = validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add armor? ")
                #     if prompt2 == "Yes" or "yes" or "y":
                #         armor1 = input("Please enter armor type: ")
                #         add_armor(hero1, armor1)
                #     elif prompt2 == "No" or "no" or "n":
                #         cont_ability = False
            else:
                cont_hero = False
                print(team_name,": ", team)

    def build_team_one(self):
        self.build_team(self.team_one)
        # team_name = build_team()

        """
    # This method should allow a user to build team one.
        """

    def build_team_two(self):
        self.build_team(self.team_two)
        """
        This method should allow user to build team two.
        """

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
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        team_one.stats
        team_two.stats
        """
        ***SHould jsut run stats method on both teams***
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

# # create heros
# team_one = superheroes.Team("One")
# jodie = superheroes.Hero("Jodie Foster")
# aliens = superheroes.Ability("Alien Friends", 10000)

# def create_ability():
#     abilities = [
#         "Alien Attack",
#         "Science",
#         "Star Power",
#         "Immortality",
#         "Grandmas Cookies",
#         "Blinding Strength",
#         "Cute Kittens",
#         "Team Morale",
#         "Luck",
#         "Obsequious Destruction",
#         "The Kraken",
#         "The Fire of A Million Suns",
#         "Team Spirit",
#         "Canada"]
#     name = abilities[random.randint(0, len(abilities) - 1)]
#     power = random.randint(45, 700000)
#     return superheroes.Ability(name, power)
#    heroes

Arena().create_heroes()
Arena().build_team_one()
