def main():
    file1 = open('5-1.txt', 'r')
    Lines = file1.readlines()
    stacks = list()
    phase = 0
    for c, l in enumerate(Lines):
        l = l.strip()
        if l == "":
            phase = 1
            numStacks = int(Lines[c - 1].strip()[-1])
            for x in range(0, numStacks):
                stacks.append(list())
            for l2 in range(0, c - 1):
                tempLine = Lines[l2].replace("\n", "")

                tc = 1
                for t in range(0, numStacks):
                    if tempLine[tc] != " ":
                        stacks[t].append(tempLine[tc])
                    tc += 4
                # 1, 5, 9
                phase = 2
        if phase == 2 and l != "":
            l3 = l.split(" ")
            iNum = int(l3[1])
            iFrom = int(l3[3])
            iTo = int(l3[5])
            tempList = list()
            for x in range(0, iNum):
                tempList.append(stacks[iFrom - 1][0])
                stacks[iFrom - 1].pop(0)
            stacks[iTo - 1] = tempList + stacks[iTo - 1]
    print(stacks)
    answer = ""
    for x in range(0, numStacks):
        answer += stacks[x][0]
    print(answer)
    #print(numStacks)
if __name__ == "__main__":
    main()