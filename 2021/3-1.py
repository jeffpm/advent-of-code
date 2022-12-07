def main():
    numbers = []
    f = open("3-1.txt", "r")
    for x in f:
        numbers.append(x)

    cols = len(numbers[0])

    gammaRate = ""
    epsilonRate = ""
    for x in range (0, cols-1):
        zeroCount = 0
        oneCount = 0
        for y in numbers:
            if int(y[x]) == 0:
                zeroCount += 1
            else:
                oneCount += 1

        if zeroCount >= oneCount:
            gammaRate += "0"
        else:
            gammaRate += "1"


    epsilonRate = ''.join(["1" if x == "0" else "0" for x in gammaRate])
    print(int(gammaRate, 2) * (int(epsilonRate, 2)))
if __name__ == "__main__":
    main()
