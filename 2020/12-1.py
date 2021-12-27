def main():
    file = open('12-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    # print(lines)

    heading = "E"
    xPos = 0
    yPos = 0
    lMap = {"N": "W", "W": "S", "S":"E", "E":"N"}
    rMap = {"N": "E", "W": "N", "S":"W", "E":"S"}

    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        if direction == "F":
            if heading == "E":
                xPos += amount
            elif heading == "N":
                yPos += amount
            elif heading == "W":
                xPos -= amount
            elif heading == "S":
                yPos -= amount
        elif direction == "N":
            yPos += amount
        elif direction == "E":
            xPos += amount
        elif direction == "S":
            yPos -= amount
        elif direction == "W":
            xPos -= amount
        elif direction == "L":
            numTimes = int(amount/90)
            for _ in range(0, numTimes):
                heading = lMap[heading]
        elif direction == "R":
            numTimes = int(amount/90)
            for _ in range(0, numTimes):
                heading = rMap[heading]

    print(f"{xPos}, {yPos}")

    distance = abs(xPos) + abs(yPos)
    print(distance)

if __name__ == "__main__":
    main()
