import fighting
import models

if __name__ == '__main__':
    rich = models.Fighter('Rich')
    rich.debug_entry(speed=1)

    rob = models.Fighter('Rob')
    rob.debug_entry(strength=17)

    winner = fighting.Fight(rich, rob)
    if winner == 1:
        print("RICH WINS!")
    else:
        print("ROB WINS!")
