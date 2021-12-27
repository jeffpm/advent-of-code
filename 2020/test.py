def main():
    processIt("000000000000000000000000000000X1101X")

def processIt(result):
    resultL = list(result)
    # print(resultL)
    if "X" in resultL:
        for count, x in enumerate(resultL):
            if x == "X":
                for y in ["0", "1"]:
                    resultL[count] = y
                    processIt(''.join(resultL))
    else:
        print(''.join(resultL))

if __name__ == "__main__":
    main()