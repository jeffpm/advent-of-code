def main():
    file = open('6-1.txt',mode='r')
    text = file.read()
    file.close()

    groups = text.split("\n\n")
    print(groups)
    groups = [group.replace("\n", "") for group in groups]
    print(groups)
    sets = []

    for group in groups:
        groupSet = set()
        for answer in group:
            groupSet.add(answer)
        # print(groupSet)
        sets.append(groupSet)

    total = 0
    for setx in sets:
        total += len(setx)

    print(total)

if __name__ == "__main__":
    main()