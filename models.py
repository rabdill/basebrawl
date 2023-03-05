import random

class Fighter:
    def __init__(self, name):
        self.name = name
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

    def debug_entry(self, health=300, strength=50, speed=3):
        self.health = health
        self.max_health = health
        self.strength = strength
        self.speed = speed

    def reset(self):
        """
        Sets a fighter's stats back to their original values, as if no
        fighting has happened
        """
        self.awake = True
        self.health = self.max_health

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
        """
        Calculates the impact of an attack against $opponent.

        Returns:
            - events: A list of strings indicating the results of each attack.
        """

        if not opponent.awake:
            return([f'{opponent.name} is out cold. {self.name} won\'t attack.'])
        if not self.awake:
            return([f'{self.name} passes out before he can attack.'])

        events = []
        # One "attack" could be multiple hits. The max number of hits is decided
        # by the fighter's speed trait.
        attacks = random.randint(1, self.speed)
        for x in range(attacks):
            dam = random.randint(0, self.strength)
            if not opponent.damage(dam):
                events.append(f'{self.name} knocks out {opponent.name} after doing {dam} damage!')
                break
            events.append(f'{self.name} hits {opponent.name} for {dam} damage! He has {opponent.health} points remaining.')
        return(events)

class Team:
    def __init__(self, name):
        self.name = name
        self.fighters = []

    def add_fighter(self, x):
        x.team = self.name
        self.fighters.append(x)
        random.shuffle(self.fighters)

    def awake(self):
        """
        Returns only the awake members of the roster. There is NO
        shuffling done in this step so the call will be deterministic.
        """
        return([x for x in self.fighters if x.awake])

    def numawake(self):
        """
        Quick helper function to count the number of awake fighters
        """
        return(len(self.awake()))
