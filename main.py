import sys

import fighting
import models
import simulation

if __name__ == '__main__':
    rich = models.Fighter('Rich')
    rich.debug_entry(speed=1, strength=50)

    nick = models.Fighter('Nick')
    nick.debug_entry(speed=3, strength=17)

    logan = models.Fighter('Logan')
    logan.debug_entry(speed=6, strength=5)

    rob = models.Fighter('Rob')
    rob.debug_entry(speed=4, strength=12)

    john = models.Fighter('John')
    john.debug_entry(speed=2, strength=24)

    hanratty = models.Fighter('Hanratty')
    hanratty.debug_entry(speed=1, strength=25, health=500)

    burps = models.Team('Burps')
    burps.add_fighter(rich)
    burps.add_fighter(nick)
    burps.add_fighter(logan)

    farts = models.Team('Farts')
    farts.add_fighter(rob)
    farts.add_fighter(john)
    farts.add_fighter(hanratty)

    # report = fighting.Rumble(burps, farts)
    # report.Scroll()
    # print(f'{report.winner} win.')

    results = simulation.Rumble(burps, farts, int(sys.argv[1]))
    print(f'\n\nBurps: {results[0]}\nFarts: {results[1]}')
