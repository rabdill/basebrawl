import math
import random

class Fighter:
    def __init__(self, name):
        self.name = name
        self.awake = True
        self.wins = []
        self.losses = []

        # Trait points
        self.health = None # current health points
        self.max_health = None # the ceiling for health points
        self.strength = None # max damage from one hit
        self.punch_whiff = None # probability (0–100) that a given hit will miss
        self.speed = None # how many hits can you get into one attack?
        self.min_hit = None # what's the floor for how much (unmodified) damage a hit can do?
        self.dodge = None

        ### Special tags
        self.meathead = False # Every hit gets more strength and less accuracy

    def print(self):
        """
        Converts a fighter's stats (and player stats) into a dictionary that can
        be recorded for display on the front-end.
        """
        x = {
            'name': self.name,
            #'player_stats': {},
            'fighter_stats': {
                'max_health': self.max_health,
                'strength': self.strength,
                'punch_whiff': self.punch_whiff,
                'speed': self.speed,
                'min_hit': self.min_hit,
                'dodge': self.dodge
            },
            'tags': []
        }

        if self.meathead:
            x['tags'].append('meathead')

        return(x)

    def convert_batter(self, data):
        """
        INPUT:
            data - Parses a single line of the statcast CSV batter data.
        """
        self.debug_entry()
        self.fancyname = '🪖 ' + self.name
        # xwoba
        # xba
        # xslg
        # xiso
        # xobp
        # brl
        # brl_percent
        # exit_velocity
        # hard_hit_percent
        # k_percent
        # bb_percent
        # whiff_percent
        # sprint_speed
        # oaa

        if data is None or data['whiff_percent'] is None:
            self.punch_whiff = 48
            print(self.name)
            return()

        self.punch_whiff = 50 / math.sqrt(int(data['whiff_percent']))
        self.speed = int(math.ceil(data['sprint_speed'] / 20))
        if self.speed < 1:
            self.speed = 1
        self.strength = int(math.ceil(data['xslg'] / 2))
        self.min_hit = int(math.floor(self.strength * (data['brl_percent'] / 100)))
        self.dodge = int(data['bb_percent'])

        # If a player slugs above average, has a below-average BA, and the
        # percentiles are more than 25 apart, label them a meathead
        if data['xslg'] > 55 and data['xba'] < 45 and data['xslg']-data['xba'] > 25:
            self.meathead = True
            self.max_health = int(math.ceil(self.max_health * 1.5))
            if self.speed > 8:
                self.speed = 5
            elif self.speed > 5:
                self.speed = 3
            else:
                self.speed = 1
            self.name += ' MEAT'

    def convert_pitcher(self, data):
        """
        INPUT:
            data - Parses a single line of the statcast CSV pitching data.
        """
        self.debug_entry()
        self.fancyname = '⚾ ' + self.name
        # xwoba
        # xba
        # xslg
        # xiso
        # xobp
        # brl
        # brl_percent
        # exit_velocity
        # hard_hit_percent
        # k_percent
        # bb_percent
        # whiff_percent
        # xera
        # fb_velocity
        # fb_spin
        # curve_spin
        if data is None or data['whiff_percent'] is None:
            self.punch_whiff = 55
            print(self.name)
            return()
        self.punch_whiff = 50 / math.sqrt(int(data['bb_percent']))
        self.speed = int(math.ceil(data['whiff_percent'] / 20))
        if self.speed < 1:
            self.speed = 1
        self.strength = int(math.ceil(data['fb_velocity'] / 2))
        self.min_hit = int(math.floor(self.strength * (data['brl_percent'] / 100)))
        self.dodge = int(data['hard_hit_percent'])

        # If a player slugs above average, has a below-average BA, and the
        # percentiles are more than 25 apart, label them a meathead
        if data['fb_velocity'] > 55 and data['bb_percent'] < 45 and data['fb_velocity']-data['bb_percent'] > 25:
            self.meathead = True
            self.max_health = int(math.ceil(self.max_health * 1.5))
            self.speed = 2
            self.name += ' PITCHMEAT'

    def debug_entry(self, health=300, strength=50, speed=3, punch_whiff=10, min_hit=1, dodge=31):
        self.health = health
        self.max_health = health
        self.strength = strength
        self.speed = speed
        self.punch_whiff = punch_whiff
        self.min_hit = min_hit
        self.dodge = dodge

    def reset(self):
        """
        Sets a fighter's stats back to their original values, as if no
        fighting has happened
        """
        self.awake = True
        self.health = self.max_health

    def reset_all(self):
        """
        Sets a fighter's stats back to their original values as above, but
        ALSO resets the fighter's records of wins and losses. Used after simulating
        lots of rumbles against a single team, before moving on to rumbles with
        another team.
        """
        self.reset()
        self.wins = []
        self.losses = []

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

    def _calculate_damage(self, opponent):
        """
        Separating out the ever-growing logic used to determine damage
        """

        # first determine if the hit lands
        minmiss = -10 if self.meathead else 1 # meatheads less likely to land
        miss = random.randint(minmiss, 100) < self.punch_whiff

        if miss:
            return(0)

        # then check if the opponent dodges it:
        dodge = random.randint(0, opponent.dodge) >= 60
        if dodge:
            return(-1)

        # Then determine how much damage is done:
        dam = random.randint(self.min_hit, self.strength)
        if self.meathead:
            dam += 10
        return(dam)

    def attack(self, opponent):
        """
        Calculates the impact of an attack against $opponent.

        Returns:
            - event: A string indicating the results of each attack.
        """

        if not opponent.awake:
            return([f'{opponent.name} is out cold. {self.name} won\'t attack.'])
        if not self.awake:
            return([f'{self.name} passes out before he can attack.'])

        # One "attack" could be multiple hits. The max number of hits is decided
        # by the fighter's speed trait.
        attacks_todo = 1
        dice = random.randint(0,10)
        if dice < self.speed:
            attacks_todo = random.randint(0, self.speed)


        cumulative_dam = 0
        attacks_done = 0
        dodged = False
        opp_awake = opponent.awake
        for x in range(attacks_todo):
            dam = self._calculate_damage(opponent)
            if dam == -1:
                dodged = True
                break
            opp_awake = opponent.damage(dam)
            if dam > 0:
                cumulative_dam += dam
                attacks_done += 1
            if not opp_awake:
                break
        if not opp_awake:
            return(f'{self.name} knocks out {opponent.name} after doing {cumulative_dam} damage in {attacks_done} hit{"s" if attacks_done > 1 else ""}!')

        if attacks_done == 0:
            descriptor = ''
            dodgemessage = '.'
            if attacks_todo == 2:
                descriptor = ' twice'
            if attacks_todo > 2:
                descriptor = f' {attacks_todo} times'
            if dodged:
                dodgemessage = f' after {opponent.name} dodges!'
            return(f'{self.name} tries to hit {opponent.name}{descriptor} but completely misses{dodgemessage}')

        descriptor = ','
        dodgemessage = '!'
        if attacks_done == 2:
            descriptor = ' twice,'
        if attacks_done > 2:
            descriptor = f' {attacks_done} times,'
        if dodged:
            dodgemessage = f', but {opponent.name} dodges away from further attacks.'
        return(f'{self.name} hits {opponent.name}{descriptor} doing {cumulative_dam} damage{dodgemessage} He has {opponent.health} points remaining.')

    def defeats(self, opponent):
        """
        Convenience function that records fighter-level entries for the winner and loser.

        Input:
            - opponent: A Fighter object
        """
        self.wins.append(opponent.name)
        opponent.losses.append(self.name)

class Team:
    def __init__(self, name):
        self.name = name
        self.roster = [] # ALL the fighters
        self.fighters = [] # The fighters in a single rumble

    def add_fighter(self, x):
        x.team = self.name
        self.roster.append(x)

    def fight_roster(self, n=15):
        """
        Picks a random team of n fighters for a given rumble
        """
        self.fighters = random.sample(self.roster, n)

    def shuffle(self):
        """
        Randomizes the fighter order in between rumbles.
        """
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
        for player in t1.roster + t2.roster:
            self.matchups[player.name] = {}
            for p2 in t1.roster + t2.roster:
                self.matchups[player.name][p2.name] = []

    def Record(self, text):
        """
        Records a string as a new event in the main event scroll.

        Input:
        text: String. The full text of an event.
        """
        self.events.append(text)

    def Record_major(self, text, team=None):
        """
        Records a string as a new event in the MAJOR event scroll.

        Input:
        text: String. The full text of an event.
        """
        if team is not None:
            if team==1:
                toprint = f'<li>{text}</li>'
            else:
                toprint = f'<li class="right">{text}</li>'
        else:
            toprint = f'<li class="center">{text}</li>'

        self.major_events.append(toprint)


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
        self.Record_major(f'{victor} of the {vteam} defeated {loser}.', team=winner)
