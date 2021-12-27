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
            # print(mask)
        else:
            val = int(line.split(" = ")[1])
            address = line.split(" = ")[0]
            result = re.search('\[(.*)\]', address)
            address = int(result.group(1))
            # print(f"address: {address} val: {val}")
            addressB = format(address, '036b')
            # print(addressB)
            addressBL = list(addressB)
            for count, x in enumerate(addressBL):
                if mask[count] == "X":
                    addressBL[count] = "X"
                elif mask[count] == "1":
                    addressBL[count] = "1"
            addressB = ''.join(addressBL)
            processIt(mem, val, addressB)
    # print(mem)
    total = 0
    for x in mem.keys():
        total += mem[x]
    print(total)

def processIt(mem, val, result):
    resultL = list(result)
    # print(resultL)
    if "X" in resultL:
        for count, x in enumerate(resultL):
            if x == "X":
                for y in ["0", "1"]:
                    resultL[count] = y
                    processIt(mem, val, ''.join(resultL))
    else:
        # print(''.join(resultL))
        mem[int(''.join(resultL), 2)] = val
if __name__ == "__main__":
    main()