import sys

import fighting
import models

if __name__ == '__main__':
    rich = models.Fighter('Rich')
    rich.debug_entry(speed=1, strength=50)

    rob = models.Fighter('Rob')
    rob.debug_entry(speed=4, strength=12)

    nick = models.Fighter('Nick')
    nick.debug_entry(speed=3, strength=17)

    john = models.Fighter('John')
    john.debug_entry(speed=2, strength=24)

    burps = models.Team('Burps')
    burps.add_fighter(rich)
    burps.add_fighter(nick)

    farts = models.Team('Farts')
    farts.add_fighter(rob)
    farts.add_fighter(john)

    fighting.Rumble(burps, farts)
