def printIt(cycle, x, printLine):
    cycle = cycle % 40
    # print(f'cycle: {cycle} x:{x}')
    if cycle - 1 == x or cycle - 1 == x -1 or cycle - 1 == x+1:
        printLine += "#"
        # print("#")
    else:
        printLine += "."
        # print(".")
    # if cycle != 1 and cycle % 40 == 1:
    #     printLine+='\n'

    return printLine
def main():
    x = 1
    cycle = 0
    printLine = ""
    
    for line in open('10-1.txt'):
        cycle += 1
        printLine = printIt(cycle, x, printLine)
        match line.split():
            case ["noop"]:
                pass
            case ["addx", step]:
                if cycle % 40 == 0:
                    print(printLine)
                    printLine = ""
                cycle += 1
                printLine = printIt(cycle, x, printLine)
                x += int(step)
        if cycle % 40 == 0:
            print(printLine)
            printLine = ""

if __name__ == "__main__":
    main()