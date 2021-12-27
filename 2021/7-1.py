def main():
    file = open('7-1.txt',mode='r')
    text = file.read()
    file.close()
    minFuel = 0

    groups = text.split("\n\n")

    crabs = [int(x) for x in groups[0].split(',')]
    # print(crabs)

    for position in range(0, max(crabs)):
        theSum = 0
        for crab in crabs:
            theSum += abs(crab-position)
        # print(f'position: {position}: sum: {theSum}')

        if minFuel == 0:
            minFuel = theSum
        else:
            if theSum < minFuel:
                minFuel = theSum

    print(f"min fuel: {minFuel}")
if __name__ == "__main__":
    main()