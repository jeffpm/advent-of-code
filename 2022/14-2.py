import numpy as np

import sys
global grid
global dropCol
np.set_printoptions(threshold=sys.maxsize)
def move(pos):
    # print(pos)
    global grid
    global dropCol
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
    if col -1 == -1 or col + 1 == len(grid[0]):
        # print(f'{row}, {col}')
        # print('need to hstack')
        tempCol = np.chararray((len(grid), 1), unicode=True)
        with np.nditer(tempCol, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = '.'
        tempCol[-1] = ['#']
        if col - 1 == -1:
            # print('stacking left')
            grid = np.hstack([tempCol, grid])
            dropCol += 1
            col += 1
        else:
            # print('stacking right')

            grid = np.hstack([grid, tempCol])
            # col -= 1
    try: 
        # print(f'row: {row} - col: {col}')
        if grid[row + 1][col] == '.' or grid[row + 1][col - 1] == '.' or grid[row + 1][col + 1] == '.':
            return move((row, col))
        else:
            grid[row][col] = 'o'
    except:
        return -1

def main():
    global grid
    global dropCol
    file1 = open('14-1.txt', 'r')
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
    
    for c in ['.', '#']:
        tempRow = list()
        for _ in range(maxCol - minCol + 1):
            tempRow.append(c)
        grid = np.vstack([grid, tempRow])

    count = 0
    colCounter = len(grid[0])
    dropCol = 500 - minCol
    while (True):
        result = move((0, dropCol))
        # if result == -1:
        #     print(count)
        #     return
        count +=1
        # print(f"move: {count}")
        # print(grid)
        # step 40 is where the flaw in the logic is shown
        if grid[0][dropCol] == "o":
            print(count)
            return
    
        
        
if __name__ == "__main__":
    main()