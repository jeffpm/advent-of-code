import numpy as np
import sys
global grid
def move(pos):
    global grid
    while grid[pos[0]][pos[1]] == '.':
        pos = (pos[0] + 1, pos[1])
    pos = (pos[0] -1, pos[1])
    if grid[pos[0] + 1][pos[1] - 1] == '.':
        row = pos[0] + 1
        col = pos[1] - 1
    elif grid[pos[0] + 1][pos[1] + 1] == '.':
        row = pos[0] + 1
        col = pos[1] + 1
    else:
        row = pos[0]
        col = pos[1]
    try:
        if grid[row + 1][col] == '.' or grid[row + 1][col - 1] == '.' or grid[row + 1][col + 1] == '.':
            return move((row, col))
        else:
            grid[row][col] = 'o'
    except:
        return -1
    
    
def main():
    global grid
    file1 = open('14-test.txt', 'r')
    Lines = file1.readlines()
    paths = list()
    minRow = 0
    maxRow = -1
    minCol = -1
    maxCol = -1
    for line in Lines:
        line = line.strip()
        p = line.split(' -> ')
        for count, _ in enumerate(p):
            if count == len(p) -1 :
                break
            point1Col, point1Row = p[count].split(',')
            point2Col, point2Row = p[count + 1].split(',')
            point1Col, point1Row, point2Col, point2Row = int(point1Col), int(point1Row), int(point2Col), int(point2Row)
            tminCol = point1Col if point1Col < point2Col else point2Col
            tmaxCol = point1Col if point1Col > point2Col else point2Col
            # tminRow = point1Row if point1Row < point2Row else point2Row
            tmaxRow = point1Row if point1Row > point2Row else point2Row
            if maxRow == -1:
                maxRow = tmaxRow
            else:
                maxRow = tmaxRow if tmaxRow > maxRow else maxRow
            if minCol == -1:
                minCol = tminCol
            else:
                minCol = tminCol if tminCol < minCol else minCol
            if maxCol == -1:
                maxCol = tmaxCol
            else:
                maxCol = tmaxCol if tmaxCol > maxCol else maxCol
            paths.append(((point1Col, point1Row), (point2Col, point2Row)))

   # normalize numbers
    for c, p in enumerate(paths):
        paths[c] = tuple(((p[0][0] - minCol, p[0][1]), (p[1][0] - minCol, p[1][1])))

    grid = np.chararray((maxRow - minRow + 1, maxCol - minCol + 1), unicode=True)
    with np.nditer(grid, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = '.'

    for p in paths:
        # if on same col, iterate row
        if p[0][0] == p[1][0]:
            start = p[0][1] if p[0][1] <= p[1][1] else p[1][1]
            end = p[0][1] if p[0][1] > p[1][1] else p[1][1]
            for row in range(start, end + 1):
                grid[row][p[0][0]] = '#'
        else:
            # if on same row, iterate col
            start = p[0][0] if p[0][0] <= p[1][0] else p[1][0]
            end = p[0][0] if p[0][0] > p[1][0] else p[1][0]
            for col in range(start, end + 1):
                grid[p[0][1]][[col]] = '#'
    
    count = 0
    while (True):
        result = move((0, 500 - minCol))
        if result == -1:
            print(count)
            return
        count +=1
        
if __name__ == "__main__":
    main()