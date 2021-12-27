import re
def main():
    file = open('14-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()

    mem = {}
    mask = ""
    val = 0
    pos = 0
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
            print(mask)
        else:
            val = int(line.split(" = ")[1])
            position = line.split(" = ")[0]
            result = re.search('\[(.*)\]', position)
            position = result.group(1)
            valString = format(val, '036b')
            print("before")
            print(valString)
            tempList = []
            for count, x in enumerate(valString):
                if mask[count] != "X":
                    tempList.append(mask[count])
                else:
                    tempList.append(valString[count])
            valString = ''.join(tempList)
            print("after")
            print(valString)
            mem[position] = int(valString,2)
    print(mem)
    total = 0
    for x in mem.keys():
        total += mem
    print(total)
if __name__ == "__main__":
    main()