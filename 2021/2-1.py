def main():
    horiz = 0
    depth = 0
    aim = 0
    f = open("2-1.txt", "r")
    for x in f:
        daSplit = x.split(" ")
        instruction = daSplit[0]
        movement = int(daSplit[1])

        if instruction == "forward":
            horiz += movement
        elif instruction == "down":
            depth += movement
        elif instruction == "up":
            depth -= movement

    print(horiz * depth)
if __name__ == "__main__":
    main()
