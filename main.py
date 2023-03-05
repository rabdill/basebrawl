import sys

import models
import simulation

if __name__ == '__main__':
    rich = models.Fighter('Rich')
    rich.debug_entry(speed=1)

    rob = models.Fighter('Rob')
    rob.debug_entry(strength=17)

    results = simulation.Fight(rich, rob, int(sys.argv[1]))
    print(f'\nRich: {results[0]}\nRob:  {results[1]}\n')
