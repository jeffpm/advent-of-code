import math
def main():
    seatIDs=[]
    with open('5-1.txt') as f:
        lines = f.read().splitlines()
    for x in lines:
        seatIDs.append(processLine(x))

    seatIDs= sorted(seatIDs, key = lambda x: x[0])
    # print(seatIDs)
    for x in range(10, 116):
        print(x)
        filtered = filter(lambda seatID: seatID[0]==x, seatIDs)
        # if len((list(filtered))) != 7:
        if (len(list(filtered))) !=8:
            print(list(filtered))

            # 82, 1, 657
def processLine(line):
    rmin = 0
    rmax = 127
    row = 0
    cmin = 0
    cmax = 7
    col = 0
    for counter, bit in enumerate(line[:7]):
        if bit == "F":
            if counter == 6:
                row = rmin
            rmax = math.floor((rmax+rmin)/2)
        elif bit == "B":
            rmin = math.ceil((rmax+rmin)/2)
            if counter == 6:
                row = rmax
    for counter, bit in enumerate(line[-3:]):
        if bit == "L":
            if counter == 2:
                col = cmin
            cmax = math.floor((cmax+cmin)/2)
        elif bit == "R":
            cmin = math.ceil((cmax+cmin)/2)
            if counter == 2:
                col = cmax
    return(row, col, (row * 8) + col)


if __name__ == "__main__":
    main()
