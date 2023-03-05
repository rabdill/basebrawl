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
