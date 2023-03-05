import random

def Fight(p1, p2):
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
        events.append(attacker.attack(defender))
        if not p1.awake or not p2.awake:
            for x in events:
                print(x)
            print('\n\nThe fight concludes!')
            if p1.awake:
                return(1)
            return(2)

        # if we go for another round, swap attacker and defender
        buffer = attacker
        attacker = defender
        defender = buffer
