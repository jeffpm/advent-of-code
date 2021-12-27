def main():
    file = open('12-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    # print(lines)

    heading = "E"
    xPos = 0
    yPos = 0
    wayXPos = 10
    wayYPos = 1
    lMap = {"N": "W", "W": "S", "S":"E", "E":"N"}
    rMap = {"N": "E", "W": "N", "S":"W", "E":"S"}

    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        if direction == "F":
            xPos += (amount * wayXPos)
            yPos += (amount * wayYPos)
        elif direction == "N":
            wayYPos += amount
        elif direction == "E":
            wayXPos += amount
        elif direction == "S":
            wayYPos -= amount
        elif direction == "W":
            wayXPos -= amount
        elif direction == "L":
            numTimes = int(amount/90)
            for _ in range(0, numTimes):
                wayYPos *= -1
                temp = wayXPos
                wayXPos = wayYPos
                wayYPos = temp
        elif direction == "R":
            numTimes = int(amount/90)
            for _ in range(0, numTimes):
                wayXPos *= -1
                temp = wayXPos
                wayXPos = wayYPos
                wayYPos = temp

    print(f"ship {xPos}, {yPos}")
    print(f"way {wayXPos}, {wayYPos}")
    distance = abs(xPos) + abs(yPos)
    print(distance)

if __name__ == "__main__":
    main()
