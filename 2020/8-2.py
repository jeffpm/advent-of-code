def main():
    with open('7-1.txt') as f:
        lines = f.read().splitlines()
        modified = set()
        # while True:
        tempLines = lines.copy()
        for counter, line in enumerate(lines):
            tempLines = lines.copy()
            # print(counter)
            if counter not in modified:
                if line[:3] == "jmp":
                    # print(f"replacing jmp with nop")
                    line = line.replace("jmp", "nop")
                    tempLines[counter] = line
                    # print(tempLines[counter])
                    modified.add(counter)
                elif line[:3] == "nop":
                    # print(f"replacing nop with jmp")
                    line = line.replace("nop", "jmp")
                    tempLines[counter] = line
                    # print(tempLines[counter])
                    modified.add(counter)
                result, sum = evaluate(tempLines)
                if result == 1:
                    print (f"result: {result}, sum: {sum}")

    
def evaluate(lines):
    # print(lines)
    linePos = 0
    accum = 0
    positions = set()
    while True:
        ins, val = lines[linePos].split(" ")
        mod = val[0]
        val = int(val[1:])
        
        if linePos in positions:
            return 0, accum
        
        positions.add(linePos)

        # print(lines[linePos])
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
        # print(f"{linePos}, {len(lines)}")
        if linePos == len(lines):
            return 1, accum

if __name__ == "__main__":
    main()