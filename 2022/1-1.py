def main():
    theSums = list()
    file1 = open('1-1.txt', 'r')
    Lines = file1.readlines()
    tempSum = 0
    maxSum = 0

    for l in Lines:
        l = l.strip()
        if l == "":
            theSums.append(tempSum)
            if tempSum > maxSum:
                maxSum = tempSum
            tempSum = 0
        else:
            tempSum += int(l)
    print(f'pt1: {maxSum}')

    theSums.sort(reverse=True)
    print(f'pt2: {(theSums[0] + theSums[1] + theSums[2])}')

if __name__ == "__main__":
    main()