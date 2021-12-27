def main():
    file = open('7-1.txt',mode='r')
    text = file.read()
    file.close()
    minFuel = 0
    cache = {}

    groups = text.split("\n\n")

    crabs = [int(x) for x in groups[0].split(',')]

    tempSum = 0
    for x in range(0, max(crabs) + 1):
        tempSum += x
        cache[x] = tempSum
    for position in range(0, max(crabs)):
        theSum = 0
        for crab in crabs:
            theRange = abs(crab-position)
            theSum += cache[theRange]
            if minFuel != 0 and theSum > minFuel:
                break
        if minFuel == 0:
            minFuel = theSum
        else:
            if theSum < minFuel:
                minFuel = theSum
    print(f"min fuel: {minFuel}")
if __name__ == "__main__":
    main()