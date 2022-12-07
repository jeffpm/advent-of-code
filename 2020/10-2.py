arrangements = set()
daSum = 1
def main():
    with open('10-1.txt') as f:
        adapters = f.read().splitlines()
    voltage = 0
    seq = []
    adapters = [int(adapter) for adapter in adapters]
    getArrangements(adapters, voltage, seq)
    print(daSum)

def getArrangements(adapters, voltage, seq):
    global daSum
    inRange = [adapter for adapter in adapters if adapter > voltage and adapter <= voltage + 3 ]
    # print(inRange)
    for adapter in inRange:
        if len(seq) > 0 and voltage<seq[-1]:
            # print("NEW SEQ")
            daSum += 1
            print(daSum)
            seq = []
        seq.append(voltage)
        # print(seq)
        getArrangements(adapters, adapter, seq)


    # tempList = []
    # for adapter in adapters:
    #     if adapter > voltage and adapter <= voltage + 3:
    #         tempList.append(adapter)

    # return min(tempList)

if __name__ == "__main__":
    main()
