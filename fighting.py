import random

def Fight(p1, p2, print_updates = True):
    """
    A one-on-one fight between two players.

    Inputs:
    - p1: a Fighter object
    - p2: a Fighter object
    - print_updates: Boolean indicating whether to print fight events to stdout

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

        if p1.awake and p2.awake:
            # if we go for another round, swap attacker and defender
            buffer = attacker
            attacker = defender
            defender = buffer
            continue

        # if we're here, the fight is over
        if print_updates:
            print('\n\n')
            for x in events:
                print(x)

        return(1 if p1.awake else 2)

def Rumble(t1, t2):
    """
    A fight between two TEAMS.

    Inputs:
    - t1: a Team object
    - t2: a Team object

    Returns:
    - winner: Integer. 1 means t1 won, 2 means t2 won.
    """
    round = 1
    while min(t1.numawake(), t2.numawake()) > 0:
        print(f'\n\n\n=========\nROUND {round}:')
        print(f'{t1.name}: {t1.numawake()} awake')
        print(f'{t2.name}: {t2.numawake()} awake\n\n')

        fights = min(t1.numawake(), t2.numawake())
        t1f = t1.awake()
        t2f = t2.awake()

        for x in range(fights):
            print(f'{x} of {fights}')
            Fight(t1f[x], t2f[x])

        round += 1
