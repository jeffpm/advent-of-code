import numpy as np
global grid
def move(pos):
    global grid
    while grid[pos[0]][pos[1]] == '.':
        pos = (pos[0] + 1, pos[1])
        # print(f'row: {pos[0]} - col: {pos[1]}')
    pos = (pos[0] -1, pos[1])
    # print(pos)
    if grid[pos[0] + 1][pos[1] - 1] == '.':
        row = pos[0] + 1
        col = pos[1] - 1
    elif grid[pos[0] + 1][pos[1] + 1] == '.':
        row = pos[0] + 1
        col = pos[1] + 1
    else:
        row = pos[0]
        col = pos[1]
    if grid[row + 1][col] == '.' or grid[row + 1][col - 1] == '.' or grid[row + 1][col + 1] == '.':
        move((row, col))
    else:
        grid[row][col] = 'o'
    
def main():
    global grid
    file1 = open('14-1.txt', 'r')
    Lines = file1.readlines()
    paths = list()
    minY = 0
    maxY = -1
    minX = -1
    maxX = -1
    for line in Lines:
        line = line.strip()
        p = line.split(' -> ')
        for count, _ in enumerate(p):
            if count == len(p) -1 :
                break
            point1x, point1y = p[count].split(',')
            point2x, point2y = p[count + 1].split(',')
            point1x, point1y, point2x, point2y = int(point1x), int(point1y), int(point2x), int(point2y)
            tminX = point1x if point1x < point2x else point2x
            tmaxX = point1x if point1x > point2x else point2x
            # tminY = point1y if point1y < point2y else point2y
            tmaxY = point1y if point1y > point2y else point2y
            if maxY == -1:
                maxY = tmaxY
            else:
                maxY = tmaxY if tmaxY > maxY else maxY
            if minX == -1:
                minX = tminX
            else:
                minX = tminX if tminX < minX else minX
            if maxX == -1:
                maxX = tmaxX
            else:
                maxX = tmaxX if tmaxX > maxX else maxX
            paths.append(((point1x, point1y), (point2x, point2y)))

    # print(paths)
    # print(f'minX: {minX} - maxX: {maxX} - minY: {minY} maxY: {maxY}')
    # normalize numbers
    for c, p in enumerate(paths):
        paths[c] = tuple(((p[0][0] - minX, p[0][1]), (p[1][0] - minX, p[1][1])))

    grid = np.chararray((maxY - minY + 1, maxX - minX + 1), unicode=True)
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
    
    # print(grid)
    count = 0
    while (True):
        move((0, 500 - minX))
        count +=1
        print(count)
if __name__ == "__main__":
    main()