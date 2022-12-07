def main():
    with open('9-1.txt') as f:
        lines = f.read().splitlines()

    preamble = 25
    val = 0
    daSum = 0
    sums = []
    for counter, line in enumerate(lines):
        if counter >= preamble:
            nums = lines[counter - preamble: counter]
            valid = False
            for xc, x in enumerate(nums):
                for yc, y in enumerate(nums):
                    if xc != yc:
                        if int(x) + int(y) == int(line):
                            valid = True
                            break
                if valid:
                    break
            if not valid:
                print(f"value {line} is a bad boi")
                val = int(line)
                break
    for counter, line in enumerate(lines):
        tempCounter = counter
        while daSum != val:
            daSum += int(lines[tempCounter])
            sums.append(int(lines[tempCounter]))
            tempCounter += 1
            if daSum > val:
                daSum = 0
                sums = []
                break
            if daSum == val:
                break

    print(sums)
    print(min(sums) + max(sums))


if __name__ == "__main__":
    main()
