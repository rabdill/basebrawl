import random

import models

def Fight(p1, p2):
    """
    A one-on-one fight between two players.

    Inputs:
    - p1: a Fighter object
    - p2: a Fighter object

    Returns:
    - winner: Integer. 1 means p1 won, 2 means p2 won.
    """

    events = []

    if p1.speed > p2.speed:
        attacker = p1
        defender = p2
    elif p2.speed > p1.speed:
        attacker = p2
        defender = p1
    else: # equal speed
        if random.randrange(2) == 0:
            attacker = p1
            defender = p2
        else:
            attacker = p2
            defender = p1
    events.append(f'<br><br>{attacker.name} attacks {defender.name}:')

    while True:
        events += attacker.attack(defender)
        if not p1.awake or not p2.awake:
            break
        # if we go for another round, swap attacker and defender
        buffer = attacker
        attacker = defender
        defender = buffer

    # if we're here, the fight is over
    if p1.awake:
        result = 1
        p1.defeats(p2)
    else:
        result = 2
        p2.defeats(p1)
    return(result, events)

def Rumble(t1, t2):
    """
    A fight between two TEAMS.

    Inputs:
    - t1: a Team object
    - t2: a Team object

    Returns:
    - winner: Integer. 1 means t1 won, 2 means t2 won.
    """
    # Then create an object to save matchup logs
    # for each fighter
    report = models.RumbleReport(t1, t2)

    round = 1
    while min(t1.numawake(), t2.numawake()) > 0:
        # Shuffle the team rosters at the beginning of each round
        t1.shuffle()
        t2.shuffle()
        report.Record_major(f'(Round {round})')
        report.Record(f'<h4>Round {round}</h4>')
        report.Record(f'<span class="team1"><strong>{t1.name}:</strong> {t1.numawake()} awake</span>')
        report.Record(f'<span class="team2"><strong>{t2.name}:</strong> {t2.numawake()} awake</span>')

        fights = min(t1.numawake(), t2.numawake())
        t1f = t1.awake()
        t2f = t2.awake()

        for x in range(fights):
            winner, fight_log = Fight(t1f[x], t2f[x])
            report.Save_fight(t1f[x], t2f[x], winner, fight_log)

        round += 1
    # rumble is over
    if t1.numawake() > 0:
        report.winner = t1.name
    else:
        report.winner = t2.name

    return(report)
