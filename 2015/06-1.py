from collections import defaultdict
import numpy
rows, cols = 1000, 1000
grid = numpy.zeros([rows, cols], dtype=int)

with open('06.txt') as f:
    insts = f.readlines()

def doLight(command, value):
    if command == "turn on":
        value = 1
    elif command == "turn off":
        value = 0
    elif command == "toggle":
        value = 1 if value == 0 else 0
    else:
        assert False
    return value

def doLight2(command, value):
    if command == "turn on":
        value += 1
    elif command == "turn off":
        if value !=0:
            value -= 1
    elif command == "toggle":
        value += 2
    else:
        assert False
    return value

for inst in insts:
    if inst.split(' ')[0] == "toggle":
        command = inst.split(' ')[0]
        startRow, startCol = [int(x) for x in inst.split(' ')[1].split(',')]
        endRow, endCol = [int(x) for x in inst.split(' ')[3].split(',')]
    else:  
        command = inst.split(' ')[0] + " " + inst.split(' ')[1]
        startRow, startCol = [int(x) for x in inst.split(' ')[2].split(',')]
        endRow, endCol = [int(x) for x in inst.split(' ')[4].split(',')]
    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol+1):
            grid[row][col] = doLight(command, grid[row][col])

print(numpy.count_nonzero(grid == 1))
theSum=0
for inst in insts:
    if inst.split(' ')[0] == "toggle":
        command = inst.split(' ')[0]
        startRow, startCol = [int(x) for x in inst.split(' ')[1].split(',')]
        endRow, endCol = [int(x) for x in inst.split(' ')[3].split(',')]
    else:  
        command = inst.split(' ')[0] + " " + inst.split(' ')[1]
        startRow, startCol = [int(x) for x in inst.split(' ')[2].split(',')]
        endRow, endCol = [int(x) for x in inst.split(' ')[4].split(',')]
    for row in range(startRow, endRow+1):
        for col in range(startCol, endCol+1):
            grid[row][col] = doLight2(command, grid[row][col])
            # theSum += grid[row][col]
print(numpy.sum(grid))
print(theSum)