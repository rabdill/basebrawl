import fighting

def Fight(p1, p2, iterations):
    results = []
    for x in range(iterations):
        p1.reset()
        p2.reset()
        results.append(fighting.Fight(p1, p2, False))
    return(
        (results.count(1), results.count(2))
    )

def Rumble(t1, t2, iterations):
    results = []
    for x in range(iterations):
        for player in t1.fighters + t2.fighters:
            player.reset()

        z = fighting.Rumble(t1, t2)
        results.append(z.winner)
    return(
        (results.count(t1.name), results.count(t2.name))
    )
