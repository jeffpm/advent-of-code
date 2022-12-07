import numpy as np

def getStraightLines(vents):
    straightVents = []
    for vent in vents:
        tempVent = ()
        if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
            straightVents.append(vent)

    return straightVents

def main():
    xMax = 0
    yMax = 0
    vents = []
    f = open("5-1.txt", "r")
    for line in f:
        split = line.strip().split(" -> ")
        first=split[0]
        second=split[1]
        vent1 = first.split(',')
        vent2 = second.split(',')
        if int(vent1[0]) > xMax:
            xMax = int(vent1[0])
        elif int(vent2[0]) > xMax:
            xMax = int(vent2[0])

        if int(vent1[1]) > yMax:
            yMax = int(vent1[1])
        elif int(vent2[1]) > yMax:
            yMax = int(vent2[1])
        vents.append((vent1, vent2))
    print(f"x max: {xMax}")
    print(f"y max: {yMax}")
    arr = np.zeros(shape=(yMax+1,xMax+1), dtype=int)
    # print(vents[0])

    straightVents = getStraightLines(vents)
    # print(straightVents)

    for vent in straightVents:
        # print(vent[0])
        # print(vent[1])

        if vent[0][0] != vent[1][0]:
            daRange = int(vent[0][0]) - int(vent[1][0])
            if daRange < 0:
                step = 1
            else:
                step = -1
            # print(f"da range {daRange}")
            # print(f"step {step}")
            for x in range(0, (daRange - step) *-1, step):
                arr[int(vent[0][0]) + x, int(vent[1][1])] = arr[int(vent[0][0]) + x, int(vent[1][1])] + 1
        else:
            daRange = int(vent[0][1]) - int(vent[1][1])
            if daRange < 0:
                step = 1
            else:
                step = -1
            # print(f"da range {daRange}")
            # print(f"step {step}")
            for x in range(0, (daRange - step) *-1, step):
                arr[int(vent[1][0]), int(vent[0][1]) + x] = arr[int(vent[1][0]), int(vent[0][1]) + x] + 1
        # print(range)
    
    # print(vents)
    occurrences = np.count_nonzero(arr >= 2)
    print(occurrences)
if __name__ == "__main__":
    main()