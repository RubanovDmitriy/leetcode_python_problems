def points(games):
    total = 0
    for x in games:
        b = [int(a) for a in x.split(':')]
        if b[0] > b[1]:
            total += 3
        elif b[0] == b[1]:
            total += 1

    return total
