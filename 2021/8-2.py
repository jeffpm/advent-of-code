def main():
    file = open('8-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()

    theMap = {}
    total = 0
    # 1 = 2
    # 4 = 4
    # 7 = 3
    # 8 = 7
    # 3 = 5 digits, 3 of which make 7
    # 2 = 5 digits, 2 of which are in 4
    # 5 = 5 digits, other 5 digit
    # 6 = 6 digits, 1 of which makes 1
    # 9 = 6 digits, 4 of which are in 4
    # 0 = 6 digits, last one


    for line in lines:
        inputs = line.split(" | ")[0].split(" ")
        outputs = line.split(" | ")[1].split(" ")
        # break
        while len(inputs) > 6:
            for count, input in enumerate(inputs):
                if len(input) == 2:
                    theMap[1] = input
                    inputs.pop(count)
                    break
                elif len(input) == 4:
                    theMap[4] = input
                    inputs.pop(count)
                    break
                elif len(input) == 3:
                    theMap[7] = input
                    inputs.pop(count)
                    break
                elif len(input) == 7:
                    theMap[8] = input
                    inputs.pop(count)
                    break
        while len(inputs) > 0:
            for count, input in enumerate(inputs):
                if len(input) == 5:
                    if sum(el in theMap[7] for el in input) == 3:
                        theMap[3] = input
                        inputs.pop(count)
                        break
                    elif sum(el in theMap[4] for el in input) == 2:
                        theMap[2] = input
                        inputs.pop(count)
                        break
                    else:
                        theMap[5] = input
                        inputs.pop(count)
                        break
                elif len(input) == 6:
                    if sum(el in theMap[1] for el in input) == 1:
                        theMap[6] = input
                        inputs.pop(count)
                        break
                    elif sum(el in theMap[4] for el in input) == 4:
                        theMap[9] = input
                        inputs.pop(count)
                        break
                    else:
                        theMap[0] = input
                        inputs.pop(count)
                        break
        # print (theMap)

        # decode
        outputString = ""
        for output in outputs:
            for key, value in theMap.items():
                if sum(el in output for el in value) == len(value) and len(output) == len(value):
                    outputString += str(key)
                    break
        total += int(outputString)

    print(total)

if __name__ == "__main__":
    main()