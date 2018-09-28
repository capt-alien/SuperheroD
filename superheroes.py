import random

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
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
        # Initialize starting values

    def add_ability(self, ability):
        self.abilities.append(ability)
        # abilities.append = ##no idea what to put here
        # Add ability to abilities list

    def add_armor(self,Armor):
        self.armors.append(Armor)
        ##add_armor to pass pytest

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



#if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print("Hero Attack: {}\n".format(hero.attack()))
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
