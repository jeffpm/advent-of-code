def main():
    with open('7-1.txt') as f:
        lines = f.read().splitlines()

    linePos = 0
    accum = 0
    positions = set()
    while True:
        ins, val = lines[linePos].split(" ")
        mod = val[0]
        val = int(val[1:])
        
        if linePos in positions:
            print(accum)
            break
        
        positions.add(linePos)

        print(lines[linePos])
        if ins == "nop":
            linePos += 1
        elif ins == "acc":
            if mod == "+":
                accum += val
            elif mod == "-":
                accum -= val
            linePos += 1
        elif ins == "jmp":
            if mod == "+":
                linePos += val
            elif mod == "-":
                linePos -= val

if __name__ == "__main__":
    main()