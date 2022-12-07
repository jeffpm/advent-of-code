import numpy as np

def updateBoards(boards, number):
    for board in boards:
        np.place(board, board == number, -1)

    return boards

def checkBoards(boards):
    for board in boards:
        if checkRows(board):
            return board
        if checkCols(board):
            return board
    return []
        
def checkRows(board):
    for row in board:
        neg = len(list(filter(lambda i: i < 0, row)))
        if neg == 5:
            print("row match found!")
            return True

    return False

def checkCols(board):
    for col in range(0, 5):
        arr = board[:, col]
        neg = len(list(filter(lambda i: i < 0, arr)))
        if neg == 5:
            print("col match found!")
            return True
    return False

def calculateScore(board):
    sum = 0
    for row in board:
        for col in row:
            if col != -1:
                sum += col
    return sum

def main():
    arr = np.empty(shape=(5,5), dtype=int)
    tracker = set()
    boards = []
    numbers = []
    rowCounter = 0

    with open('4-1.txt', 'r') as f:
        for count, line in enumerate(f):
            # print (line.strip())
            if count == 0:
                numbers = [int(x) for x in line.split(",")]
            elif line.strip() == "":
                arr = np.empty(shape=(5,5), dtype=int)
                rowCounter = 0
            else:
                temp = line.strip().split(" ")
                temp = list(filter(('').__ne__, temp))
                arr[rowCounter] = temp
                rowCounter += 1
                if rowCounter == 4:
                    boards.append(arr)
    print(numbers)
    for number in numbers:
        boards = updateBoards(boards, number)
        # print(boards)
        # print(boards[0][:][0])
        board = checkBoards(boards)
        if len(board) != 0:
            print(board)
            sum = calculateScore(board)
            print(sum)
            print(number)
            print(sum * int(number))
            break
    # print(boards)
if __name__ == "__main__":
    main()


