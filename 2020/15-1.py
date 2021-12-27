def main():
    daList = []
    file = open('15-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    daList = lines[0].split(",")
    daList = [int(x) for x in daList]
    # print(daList)
    turnCount = 2020

    for count in range(0, turnCount - len(daList)):
        # print(count)
        lastNum = daList[-1]
        if daList.count(lastNum) == 1:
            daList.append(0)
        elif daList.count(lastNum) > 1:
            pos1, pos2 = -1, -1
            for count, i in enumerate(daList[::-1]):
                if i == lastNum:
                    if pos1 == -1:
                        pos1 = count
                    elif pos2 == -1:
                        pos2 = count
                    else:
                        break
            # print(f"{pos1}, {pos2}")
            diff = pos2 - pos1
            daList.append(diff)
        # print(daList)
    print(daList[-1])
if __name__ == "__main__":
    main()