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


class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = list()
        # Initialize starting values

    def add_ability(self, ability):
        self.abilities.append(ability)

        # abilities.append = ##no idea what to put here
        # Add ability to abilities list

    def attack(self):
        total_attack = 0
        for item in self.abilities:
            total_attack += item.attack()
        return total_attack
        # Run attack() on every ability hero has

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
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for i, o in enumerate(self.heroes):
            if o.name == name:
                self.heroes.pop(i)
        return 0


    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if name == hero.name:
                return hero
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for Hero in self.heroes:
            print(Hero.name)

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
