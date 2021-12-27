def main():
    file = open('17-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    z = 1
    w = 1
    actives = set()
    
    for ycount, line in enumerate(lines):
        for xcount, point in enumerate(line):
            if point == "#":
                actives.add((xcount, ycount, z, w))

    # print(actives)
    for x in range(0, 6):
        newActives = set()
        allNeighbors = set()
        for cube in actives:
            allNeighbors.update(getNeighbors(cube))

        for neighbor in allNeighbors:
            count = 0
            for active in actives:
                if active != neighbor:
                    if isNeighbor(neighbor, active):
                        count += 1
            if neighbor in actives:
                if count == 2 or count == 3:
                    newActives.add(neighbor)
            else:
                if count == 3:
                    newActives.add(neighbor)
        # print(newActives)
        actives = newActives
    print(len(actives))

def isNeighbor(cube1, cube2):
    return (
        (cube2[0] >= cube1[0] - 1 and cube2[0] <= cube1[0] + 1) 
        and (cube2[1] >= cube1[1] - 1 and cube2[1] <= cube1[1] + 1)
        and (cube2[2] >= cube1[2] - 1 and cube2[2] <= cube1[2] + 1)
        and (cube2[3] >= cube1[3] - 1 and cube2[3] <= cube1[3] + 1)
        )
def getNeighbors(cube):
    neighbors = set()
    x, y, z, w = cube[0], cube[1], cube[2], cube[3]
    for x1 in range(x-1, x+2):
        for y1 in range(y-1, y+2):
            for z1 in range(z-1, z+2):
                for w1 in range(w-1, w+2):
                    neighbors.add((x1, y1, z1, w1))
    return neighbors
if __name__ == "__main__":
    main()