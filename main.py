import fighting
from models import Fighter, Team

if __name__ == '__main__':
    rich = Fighter('Rich','Alphas')
    rich.debug_entry()
    rob = Fighter('Rob','Betas')
    rob.debug_entry()

    winner = fighting.Fight(rich, rob)
    if winner == 1:
        print("RICH WINS!")
    else:
        print("ROB WINS!")
