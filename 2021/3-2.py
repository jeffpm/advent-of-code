def main():
    numbers = []
    origNumbers = []
    oxyFiltered = []
    co2Filtered = []
    oxyValue = 0
    co2Value = 0
    filter = 0
    f = open("3-1.txt", "r")
    for x in f:
        numbers.append(x)

    cols = len(numbers[0])
    origNumbers = numbers.copy()

    for x in range (0, cols-1):
        zeroCount = 0
        oneCount = 0
        for y in numbers:
            if int(y[x]) == 0:
                zeroCount += 1
            else:
                oneCount += 1

        if zeroCount > oneCount:
            filter = 0
        else:
            filter = 1
        print(f"filter {filter}")
        for z in numbers:
            # print(z)
            if int(z[x]) == filter:
                oxyFiltered.append(z)
        print(oxyFiltered)
        if len(oxyFiltered) == 1:
            oxyValue = int(oxyFiltered[0].strip(),2)
            break
        numbers = oxyFiltered
        oxyFiltered = []

    numbers = origNumbers

    for x in range (0, cols-1):
        zeroCount = 0
        oneCount = 0
        for y in numbers:
            if int(y[x]) == 0:
                zeroCount += 1
            else:
                oneCount += 1

        if zeroCount > oneCount:
            filter = 0
        else:
            filter = 1
        print(f"filter {filter}")
        for z in numbers:
            # print(z)
            if int(z[x]) != filter:
                co2Filtered.append(z)
        print(co2Filtered)
        if len(co2Filtered) == 1:
            co2Value = int(co2Filtered[0].strip(),2)
            break
        numbers = co2Filtered
        co2Filtered = []

    print(oxyValue * co2Value)
if __name__ == "__main__":
    main()
