import random

# HERO class. Stores the hero abilities, armors, calculates attack and defense values, how to deal damage, adding of kills
class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    # Add abilities into HERO.abilities. Will later be prompted for names by user and random values picked.
    def add_ability(self, ability):
        self.abilities.append(ability)

    # Adds total attack based on abilities given. Will later be prompted for names by user and random values picked.
    def attack(self):
        total_attack = 0
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

    # Adds total defense based on armors given. Will later be prompted for names by user and random values picked.
    def defend(self):
        total_defense = 0
        for add_defense in self.armors:
            total_defense += add_defense.defend()
        if self.health == 0:
            total_defense = 0
        return total_defense

    # Damage calculation. If health <= 0, death counter + 1
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    # function to add kills
    def add_kill(self, num_kills):
        self.kills += num_kills

    #Not in tutorial
    def add_armor(self, armor):
        self.armors.append(armor)

# ABILITY class. Updates attack strength based on abilities given
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    # generates random value for attack damage range (lowest, highest)
    def attack(self):
        self.lowest_attack = self.attack_strength // 2
        self.highest_attack = random.randint(self.lowest_attack, self.attack_strength)
        return self.highest_attack

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

# TEAM class. Creates teams of heroes and their attack powers
class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for index in self.heroes:
           print(index.name)

    # calculates total attack power of all heroes and calculates deaths
    def attack(self, other_team):
        total_attack_power = 0
        for hero in self.heroes:
            total_attack_power += hero.attack()
        deaths = other_team.defend(total_attack_power)

        for hero in self.heroes:
            hero.add_kill(deaths)

    # calculates total defense of all heroes and returns excess as damage to next hero
    # Ex: Hero1 has 100 health and takes 101 damage. Hero2 takes the extra 1 damage
    def defend(self, damage_amt):
        total_defense_power = 0
        for hero in self.heroes:
            total_defense_power += hero.defend()
        total_excess = damage_amt - total_defense_power
        if total_excess > 0:
            return self.deal_damage(total_excess)
        else:
            return 0

    def deal_damage(self, damage):
        total_damage = damage // len(self.heroes)
        total_deaths = 0
        for hero in self.heroes:
            hero.take_damage(total_damage)
            #does not update total damage?
            if hero.health <= 0:
                total_deaths += 1
        return total_deaths

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            print(hero + "Kill/Death Ratio:")
            print(hero.deal_damage()/hero.take_damage())

    def update_kills(self):
        for hero in self.heroes:
            if hero.add_kill:
                print(hero + " has killed another hero!")

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    # Not in tutorial. function for gathering all the user inputs for the heroes and gives them random powers solely for less user input
    def create_hero(self):
        prompt_hero = input("What hero would you like to add to Team One?")
        hero = Hero(prompt_hero)

        prompt_weapon = input("What weapon does " + prompt_hero + " have?")
        weapon = Weapon(prompt_weapon, random.randint(1,20))

        prompt_ability = input("What ability does " + prompt_hero + "have?")
        ability_power = random.randint(1,20)
        ability = Ability(prompt_ability, ability_power)

        prompt_armor = input("What armor does " + prompt_hero + " have?")
        armor_power = random.randint(1,20)
        armor = Armor(prompt_armor, armor_power)

        # self.add_hero_to_team(hero)
        hero.add_ability(ability)
        hero.add_ability(weapon)
        hero.add_armor(armor)
        return hero

    def add_hero_to_team(self, team, hero):
        print("Team:")
        print(team)
        print("Hero: ")
        print(hero)
        team.add_hero(hero)


    def build_team_one(self):
        self.team_one = Team(input("What would you like Team One to be called?"))

        count = 0
        while count < 3:
            hero = self.create_hero()
            self.add_hero_to_team(self.team_one, hero)
            print(self.team_one.heroes)
            # self.team_one.add_hero(hero)
            count += 1

        # if len(self.team_one) < 3:
        # for index, hero in enumerate(self.team_one):
        #     if index < 3:
        #         prompt_hero = input("What hero would you like to add to Team One?")
        #         print(prompt_hero + "has been added to Team One")
        #         hero.team_one.add_hero(prompt_hero)
        #         prompt_ability = input("Alright what abilities should this hero have?")
        #         print("{} now has the ability {}".format(prompt_hero, prompt_ability))
        #         hero.team_one.add_ability(prompt_ability)

    def build_team_two(self):
        self.team_two = Team(input("What would you like Team One to be called?"))

        count = 0
        while count < 3:
            hero = self.create_hero()
            self.add_hero_to_team(self.team_two, hero)
            print(self.team_two.heroes)
            # self.team_one.add_hero(hero)
            count += 1

        # self.team_two = Team(input("What would you like Team Two to be called?"))
        # for hero in range(0,3):
        #     prompt_hero = input("What hero would you like to add to Team Two?")
        #     print(prompt_hero + "has been added to Team Two")
        #     hero.team_two.add_hero(prompt_hero)
        #     prompt_ability = input("Alright what abilities should this hero have?")
        #     print("{} now has the ability {}".format(prompt_hero, prompt_ability))
        #     hero.team_two.add_ability(prompt_ability)

    def team_battle(self):
        turn_order = random.randint(0,1)
        if turn_order == 0:
            # team_one.initialize()
            print("Team One will start!")
            for i in range(0,len(self.team_one.heroes)):
                print(self.team_one.heroes)
                print(self.team_one.heroes[i].abilities)
                while self.team_one.heroes[i].health > 0 and self.team_two.heroes[i].health > 0:
                    self.team_one.attack(self.team_two)
                    self.team_two.defend(self.team_one)
                    self.team_one.update_kills()
                    self.team_two.update_kills()
            # for hero in team_one.heroes:
            #     while self.team_one.isAlive() == True and self.team_two.isAlive() == True:
            #         hero.attack(team_two)
            #         hero.defend(team_one)
            #         self.team_one.update_kills()
            #         self.team_two.update_kills()


        else:
            print("Team Two will start!")
            for i in range(0,len(self.team_two.heroes)):
                print(self.team_one.heroes)
                print(self.team_one.heroes[i].abilities)
                while self.team_one.heroes[i].health > 0 and self.team_two.heroes[i].health > 0:
                    self.team_two.attack(self.team_one)
                    self.team_one.defend(self.team_two)
                    self.team_one.update_kills()
                    self.team_two.update_kills()

            # team_two.initialize()
            # print("Team Two will start!")
            # for hero in team_one.heroes:
            #     while self.team_one.isAlive() == True and self.team_two.isAlive() == True:
            #         hero.attack(team_two)
            #         hero.defend(team_one)
            #         self.team_one.update_kills()
            #         self.team_two.update_kills()
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        for hero in self.team_one.heroes:
            hero.stats()
        for hero in self.team_two.heroes:
            hero.stats()
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

# def initialize():
if __name__ == "__main__":
    game_running = True

    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

# initialize()

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

# team = Team("yo")
# jodie = Hero("Jodie Foster")
# batman = Hero("Batman")
# ww = Hero("Wonder Woman")

# team.add_hero(jodie)
# team.add_hero(batman)
# team.add_hero(ww)
# print(len(team.heroes))

# team.remove_hero(jodie)

# print(len(team.heroes))
