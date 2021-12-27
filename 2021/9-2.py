import numpy as np

def travel(board, row, col):
    if board[row][col] == 9:
        return
    
    print(board[row][col])
    # up
    if row > 0:
        travel(board, row - 1, col)
        return
    # left
    if col > 0:
        travel(board, row, col - 1)
        return
    # right
    if col < len(board[0]) - 1:
        travel(board, row, col + 1)
        return
    # down
    if row < len(board) - 1:
        travel(board, row + 1, col)
        return

    return

def main():
    file = open('9-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    numRows = len(lines)
    numCols = len(lines[0])
    theSum = 0

    theArr = np.zeros((numRows, numCols), dtype=int)
    for count, line in enumerate(lines):
        theArr[count] = list(line)
    travel(theArr, 0, 0)
    # for row in range(numRows):
    #     for col in range(numCols):
    #         lowest = True
    #         cur = theArr[row][col]
    #         # check up
    #         if row > 0:
    #             if cur >= theArr[row-1][col]:
    #                 lowest = False
    #         # check left
    #         if col > 0:
    #             if cur >= theArr[row][col-1]:
    #                 lowest = False
    #         # check right
    #         if col < numCols - 1:
    #             if cur >= theArr[row][col+1]:
    #                 lowest = False
    #         # check down
    #         if row < numRows - 1:
    #             if cur >= theArr[row+1][col]:
    #                 lowest = False
            
    #         if lowest:
    #             theSum += (cur + 1)

    # print(theSum)

if __name__ == "__main__":
    main()