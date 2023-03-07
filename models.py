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
        attacks_todo = random.randint(1, self.speed)

        cumulative_dam = 0
        attacks_done = 0
        for x in range(attacks_todo):
            dam = random.randint(0, self.strength)
            cumulative_dam += dam
            attacks_done += 1
            opp_awake = opponent.damage(dam)
            if not opp_awake:
                break
        if not opp_awake:
            events.append(f'{self.name} knocks out {opponent.name} after doing {dam} damage in {attacks_done} hit{"s" if attacks_done > 1 else ""}!')
            return(events)

        descriptor = ','
        if attacks_done == 2:
            descriptor = ' twice,'
        if attacks_done > 2:
            descriptor = f' {attacks_done} times,'
        events.append(f'{self.name} hits {opponent.name}{descriptor} doing {dam} damage! He has {opponent.health} points remaining.')

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

class RumbleReport:
    """
    Stores the results of a team vs team matchup.
    """
    def __init__(self, t1, t2):
        self.t1 = t1.name
        self.t2 = t2.name
        self.events = []
        self.major_events = []
        self.winner = None

        self.matchups = {}
        for player in t1.fighters + t2.fighters:
            self.matchups[player.name] = {}
            for p2 in t1.fighters + t2.fighters:
                self.matchups[player.name][p2.name] = []

    def Record(self, text):
        """
        Records a string as a new event in the main event scroll.

        Input:
        text: String. The full text of an event.
        """
        self.events.append(text)

    def Scroll(self):
        """
        Prints out all events recorded for the rumble.
        """

        for x in self.events:
            print(x)
        print('\n\nSummary:')
        for x in self.major_events:
            print(x)

    def Save_fight(self, f1, f2, winner, events):
        """
        Ingests the events log from a one-on-one fight and saves the events
        both to the one long scroll (self.events) and the player-level lookups.

        Input:
        f1: String. Name of fighter 1.
        f2: String. Name of fighter 2.
        events: List of strings. Each an event in a fight between two fighters.
        """
        self.events += events
        self.matchups[f1.name][f2.name].append(events)

        if winner == 1:
            victor = f1.name
            vteam = f1.team
            loser = f2.name
        else:
            victor = f2.name
            vteam = f2.team
            loser = f1.name
        self.major_events.append(f'{victor} of the {vteam} defeated {loser}.')
