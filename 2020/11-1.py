import collections
import numpy as np
def main():
    with open('11-1.txt') as f:
        lines = f.read().splitlines()

    currGrid = np.empty((len(lines), len(lines[0])), dtype=str)
    for rcount, row in enumerate(lines):
        for ccount, col in enumerate(row):
            currGrid[rcount][ccount] = col

    newGrid = currGrid.copy()
    counter = 0
    while True:
        currGrid = newGrid.copy()
        for rcount, _ in enumerate(lines):
            for ccount, _ in enumerate(row):
                newGrid[rcount][ccount]=getNeighbors(currGrid, rcount, ccount)
        if (newGrid == currGrid).all():
            break
        counter += 1
    print(np.count_nonzero(newGrid == "#"))

def getNeighbors(grid, rpos, cpos):
    seat = grid[rpos][cpos]
    if seat == "L":
        newSeat = "#"
    elif seat == "#":
        newSeat = "L"
    else:
        return "."
    neighbors = []
    moves = [(-1, 0), (1,0), (0, -1), (0, 1), 
    (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for move in moves:
        if (len(grid) > rpos+move[0] >= 0) and (len(grid[0]) >cpos+move[1] >= 0):
            neighbors.append(grid[rpos+move[0]][cpos+move[1]])
        if seat == "L":
            if neighbors.count("#") > 0:
                return "L"
        elif seat == "#":
            if neighbors.count("#") >= 4:
                return "L"
    if seat == "L" and neighbors.count("#") == 0:
        return "#"

    return seat

if __name__ == "__main__":
    main()