import random

class Fighter:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.awake = True
        pass

    def convert_batter(self, data):
        """
        INPUT:
            data - Parses a single line of the statcast CSV batter data.
        """
        pass

    def convert_pitcher(self, data):
        """
        INPUT:
            data - Parses a single line of the statcast CSV pitching data.
        """

    def debug_entry(self):
        self.health = 100
        self.strength = 50
        self.speed = 50

    def damage(self, hit):
        """
        Subtracts a set number of health points and determines whether the
        fighter is knocked out.

        Returns:
            - self.awake: Indicating whether the hit knocked out the fighter
        """
        self.health -= hit
        if self.health <= 0:
            self.awake = False
        return(self.awake)

    def attack(self, opponent):
        dam = random.randrange(self.strength)
        if not opponent.damage(dam):
            return(f'{self.name} knocks out {opponent.name} after doing {dam} damage!')
        return(f'{self.name} hits {opponent.name} for {dam} damage! He has {opponent.health} points remaining.')

class Team:
    def __init__(self, name):
        self.name = name
        self.fighters = []

    def add(self, name):
        """
        Adds a player to the team's roster
        """
        self.fighters.append(name)

    def survey_fighters(self):
        """
        Checks the current state of all member fighters and updates team-level
        metrics such as how many members are awake.
        """
        pass