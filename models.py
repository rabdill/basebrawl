class Fighter:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.status = 'awake'
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

class Team:
    def __init__(self, name):
        self.name = name
        self.fighters = []

    def survey_fighters(self):
        """
        Checks the current state of all member fighters and updates team-level
        metrics such as how many members are awake.
        """
        pass