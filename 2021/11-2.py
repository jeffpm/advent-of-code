import numpy as np

def flash(theArr, flashCount, flashers):
    numRows = len(theArr)
    numCols = len(theArr[0])
    didFlash = False
    for r in range(numRows):
        for c in range(numCols):
            if theArr[r][c] > 9:
                didFlash = True
                flashCount += 1
                theArr[r][c] = 0
                flashers.add((r, c))
                # flash up
                if r > 0:
                    if theArr[r-1][c] != 0: theArr[r-1][c] += 1
                # up right
                if r > 0 and c < numCols - 1:
                    if theArr[r-1][c+1] != 0: theArr[r-1][c+1] += 1
                # right
                if c < numCols - 1:
                    if theArr[r][c+1] != 0: theArr[r][c+1] += 1
                # down right
                if r < numRows -1 and c < numCols - 1:
                    if theArr[r+1][c+1] !=0: theArr[r+1][c+1] += 1
                # down
                if r < numRows -1:
                    if theArr[r+1][c] !=0: theArr[r+1][c] += 1
                # down left
                if r < numRows -1 and c > 0:
                    if theArr[r+1][c-1] != 0: theArr[r+1][c-1] += 1
                # left
                if c > 0:
                    if theArr[r][c-1] != 0 : theArr[r][c-1] += 1
                # up left
                if r > 0 and c > 0:
                    if theArr[r-1][c-1] != 0: theArr[r-1][c-1] += 1
    return theArr, didFlash, flashCount, flashers

def main():
    flashers = set()
    flashCount = 0
    file = open('11-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()

    numRows = len(lines)
    numCols = len(lines[0])
    theArr = np.zeros((numRows, numCols), dtype=int)

    for count, line in enumerate(lines):
        theArr[count] = list(line)

    steps=10000000000
    doStop = False
    for x in range(steps):
        flashers = set()

        # increase energy of all by 1
        for r in range(numRows):
            for c in range(numCols):
                theArr[r][c] += 1
        didFlash = True
        # while (didFlash):
        #     if (theArr >= 9).sum() > 0:
        #         theArr, didFlash=flash(theArr)
            
        #     print(theArr)

        while (didFlash):
            theArr, didFlash, flashCount, flashers=flash(theArr, flashCount, flashers)
            if len(flashers) == numCols * numRows:
                print(x+1)
                doStop = True
                break
        if doStop:
            break
    # print(theArr)
    # print(flashCount)

            # if not didFlash:
            #     break

        # print("")
        # theArr, didFlash=flash(theArr)
        # print(theArr)
        # print(didFlash)

        # print("")
        # theArr, didFlash=flash(theArr)
        # print(theArr)
        # print(didFlash)



if __name__ == "__main__":
    main()