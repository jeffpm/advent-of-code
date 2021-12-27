import numpy as np


def main():
    file = open('11-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    numRows = len(lines)
    numCols = len(lines[0])
    theArr = np.zeros((numRows, numCols), dtype=int)

    for count, line in enumerate(lines):
        theArr[count] = list(line)

    print(theArr)

if __name__ == "__main__":
    main()