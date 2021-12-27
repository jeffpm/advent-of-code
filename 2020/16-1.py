import re

def main():
    daList = []
    file = open('16-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    valids = set()
    myTicket = []
    errorRate = 0

    part1 = True
    part2 = False
    part3 = False
    for line in lines:
        if part1:
            m = re.findall(r"([0-9]*-[0-9]*)", line)
            for x in m:
                start = int(x.split("-")[0])
                stop = int(x.split("-")[1])
                for y in range(start, stop+1):
                    valids.add(y)
        elif part2:
            myTicket = [int(x) for x in line.split(",")]
            part2 = False
        elif part3:
            tempTicket = [int(x) for x in line.split(",")]
            for x in tempTicket:
                if x not in (valids):
                    errorRate += x
            
        if line == "your ticket:":
            part1 = False
            part2 = True

        if line == "nearby tickets:":
            part2 = False
            part3 = True

    print(errorRate)
if __name__ == "__main__":
    main()