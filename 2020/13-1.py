def main():
    file = open('13-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    earliestDepart = int(lines[0])
    buses = {}
    for bus in lines[1].split(","):
        if bus != "x":
            buses[bus] = 0
    print(buses)
    while not checkTimes(earliestDepart, buses):
        continue

def checkTimes(earliestDepart, buses):
    temp = {}
    for bus in buses.keys():
        buses[bus] = int(bus) + buses[bus]
        if buses[bus] >= earliestDepart:
            temp[bus] = buses[bus]
    if len(temp) == 1:
        print("BUS FOUND!")
        print(temp)
        for bus in temp.keys():
            print((temp[bus] - earliestDepart) * int(bus))
        return True
    elif len(temp) > 1:
        print("busses found, but i don't have the smarts to handle multiple!")
        print(temp)
        return True
    else:
        return False


if __name__ == "__main__":
    main()