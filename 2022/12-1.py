import numpy as np
global minSteps
minSteps = -1
def navigate(pos, grid, steps):
    global minSteps
    steps = steps.copy()
    steps.add(pos)
    chars = "SabcdefghijklmnopqrstuvwxyzE"
    newPos = [
        (pos[0], pos[1] - 1), # left
        (pos[0] - 1, pos[1]), # up
        (pos[0], pos[1] + 1), # right
        (pos[0] + 1, pos[1]) # down
    ]
    if grid[pos[0], pos[1]] == "E":
        print("MADE IT!!!")
        # print(steps)
        print(len(steps) - 1)
        if minSteps == -1:
            minSteps = len(steps) - 1
        else:
            if len(steps) - 1 < minSteps:
                minSteps = len(steps) - 1
    # print(f'current: {pos} potential steps: {newPos}')
    tPos = list()
    # check left
    for n in newPos:
        # print(f'checking pos {n}')
        # skip if already visited
        if n in steps:
            # if pos == (3, 2):
            #     print(f"{n} skipping because already in")
            continue
        # skip if out of bounds
        if n[0] == -1 or n[0] == len(grid) or n[1] == -1 or n[1] == len(grid[0]):
            # if pos == (3, 2):
            #     print(f"{n} skipping because out of bounds")
            continue
        # skip if not viable move
        if chars.index(grid[n[0], n[1]]) > chars.index(grid[pos[0], pos[1]]) + 1:
            # if pos == (3, 2):
            #     print(f"{n} skipping because not viable")
            continue
        # tPos.append(n)
        # print(f'navigating to {n} ({grid[n[0], n[1]]}). previous steps: {steps}')
        
        navigate(n, grid, steps)
    # for c, n in enumerate(tPos.copy()):
    #     if chars.index(grid[n[0], n[1]]) == chars.index(grid[pos[0], pos[1]]) + 1:
    #         print(f'navigating to {n} ({grid[n[0], n[1]]}). previous steps: {steps}')
    #         navigate(n, grid, steps)
    #         tPos.pop(c)

    # for n in tPos:
    #     print(f'navigating to {n} ({grid[n[0], n[1]]}). previous steps: {steps}')
    #     navigate(n, grid, steps)



    # if pos[1] > 0:
    #     if (pos[0], pos[1] - 1) not in steps:
    #     # check not in steps
    #     # check in bounds
    #     # check can move
    # # check up
    # if pos[0] > 0:
    #     # check not in steps
    #     # check in bounds
    #     # check can move
    # # check right
    # if pos[1] < len(grid[0]) - 1:
    #     # check not in steps
    #     # check in bounds
    #     # check can move
    # # check down
    # if pos[0] < len(grid[0]) - 1:
    #     # check not in steps
    #     # check in bounds
    #     # check can move
def main():
    global minSteps
    file1 = open('12-1.txt', 'r')
    Lines = file1.readlines()
    numRows = len(Lines)
    numCols = len(Lines[0]) - 1
    grid = np.zeros((numRows, numCols), str)
    start = (-1, -1)
    steps = set()
    for r, l in enumerate(Lines):
        l = l.strip()
        for c, x in enumerate(l):
            grid[r][c] = x
            if x == 'S':
                start = (r, c)

    # print(grid)
    # print(start)
    # steps.add(start)
    navigate(start, grid, steps)
    print(minSteps)
if __name__ == "__main__":
    main()