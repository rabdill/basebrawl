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
    events.append(f'{attacker.name} gets the jump on {defender.name} and attacks first:')

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
    # First we create an object to save matchup logs
    # for each fighter
    report = models.RumbleReport(t1, t2)

    round = 1
    while min(t1.numawake(), t2.numawake()) > 0:
        report.Record(f'\n\n\n=========\nROUND {round}:')
        report.Record(f'{t1.name}: {t1.numawake()} awake')
        report.Record(f'{t2.name}: {t2.numawake()} awake\n\n')

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
