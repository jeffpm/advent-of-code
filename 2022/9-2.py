def moveTail(hx, hy, tx, ty):
    #check if touching
    if max([abs(hx - tx), abs(hy - ty)]) <= 1:
        return (tx, ty)

    # check if on same x or y axis
    if hy == ty or hx == tx:
        if hy == ty:
            if hx > tx:
                tx += 1
            else:
                tx -= 1
        elif hx == tx:
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        return (tx, ty)

    # diagonals
    # up right
    if hx > tx and hy > ty:
        tx += 1
        ty += 1
    # up left
    elif hx < tx and hy > ty:
        tx -= 1
        ty += 1
    # down right
    elif hx > tx and hy < ty:
        tx += 1
        ty -= 1
    # down left
    elif hx < tx and hy < ty:
        tx -= 1
        ty -= 1
    return (tx, ty)
    
    

def main():
    tailPos = set()
    knots = list()
    for x in range (0, 10):
        knots.append((0, 0))
    # hx = hy = tx = ty = 0
    for line in open('9-1.txt'):
        tailPos.add((0,0))
        
        d, n = line.split()
        n = int(n)
        hx = knots[0][0]
        hy = knots[0][1]
        for z in range(0,n):
            if d == "U":
                hy += 1
            elif d == "D":
                hy -= 1
            elif d == "L":
                hx -= 1
            elif d == "R":
                hx += 1
            knots[0] = (hx, hy)
            for x in range(1, 10):
                ans = moveTail(knots[x-1][0], knots[x-1][1], knots[x][0], knots[x][1])
                knots[x] = (ans[0], ans[1])
            tailPos.add((knots[9][0], knots[9][1]))
    print(len(tailPos))
        


if __name__ == "__main__":
    main()