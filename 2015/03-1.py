with open('03.txt') as f:
    line = f.readline()
    x = 0
    y = 0
    houses = []
    houses.append((x,y))
    for d in line:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '>':
            x += 1
        elif d == '<':
            x -= 1
        houses.append((x, y))
    print(len(set(houses)))

    sx = 0
    sy = 0
    rx = 0
    ry = 0
    houses = []
    houses.append((sx,sy))
    for count, d in enumerate(line):
        if count % 2 == 0:
            if d == '^':
                sy += 1
            elif d == 'v':
                sy -= 1
            elif d == '>':
                sx += 1
            elif d == '<':
                sx -= 1
            houses.append((sx, sy))
        else:
            if d == '^':
                ry += 1
            elif d == 'v':
                ry -= 1
            elif d == '>':
                rx += 1
            elif d == '<':
                rx -= 1
            houses.append((rx, ry))
    print(len(set(houses)))