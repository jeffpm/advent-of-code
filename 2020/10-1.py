def main():
    usedAdapters = []
    with open('10-1.txt') as f:
        adapters = f.read().splitlines()
    voltage = 0
    differences = {}

    adapters = [int(adapter) for adapter in adapters]
    while(True):
        print(voltage)
        voltage, difference = (getNearestAdapter(adapters, voltage))
        print(f"v: {voltage} d: {difference}")
        if difference not in differences:
            differences[difference] = 1
        else:
            differences[difference] += 1
        if voltage == max(adapters):
            voltage += 3
            difference = 3
            if difference not in differences:
                differences[difference] = 1
            else:
                differences[difference] += 1
            print(voltage)
            print(differences)
            print(differences[1] * differences[3])
            break

def getNearestAdapter(adapters, voltage):
    tempList = []
    for adapter in adapters:
        if adapter > voltage and adapter <= voltage + 3:
            tempList.append(adapter)

    return min(tempList), min(tempList) - voltage

if __name__ == "__main__":
    main()
