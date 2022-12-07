def main():
    counter = 0
    with open('2-1.txt') as f:
        lines = f.read().splitlines()
    for x in lines:
        if processLine(x):
            counter += 1

    print(counter)

def processLine(line):
    segments = line.split(" ")

    min, max = segments[0].split("-")
    min, max = int(min), int(max)
    char = segments[1].split(":")[0]
    password = segments[2]
    summer = 0

    if password[min-1] == char:
        summer += 1

    if password[max-1] == char:
        summer += 1

    if summer != 1:
        return False
    else:
        return True
if __name__ == "__main__":
    main()
