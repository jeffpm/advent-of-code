def main():
    file = open('13-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    earliestDepart = int(lines[0])
    buses = {}
    for count, bus in enumerate(lines[1].split(",")):
        if bus != "x":
            buses[bus] = (count, int(bus))
    print(buses)
    while not checkTimes(buses):
        continue

def checkTimes(buses):
    for bus in buses.keys():
        delay, time = buses[bus]
        time = time + delay + int(bus)
        buses[bus] = (delay, time)
        
    print(buses)
    # if len(temp) == 1:
    #     print("BUS FOUND!")
    #     print(temp)
    #     for bus in temp.keys():
    #         print((temp[bus] - earliestDepart) * int(bus))
    #     return True
    # elif len(temp) > 1:
    #     print("busses found, but i don't have the smarts to handle multiple!")
    #     print(temp)
    #     return True
    # else:
    #     return False


if __name__ == "__main__":
    main()