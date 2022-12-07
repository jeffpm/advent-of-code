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

    charCount = password.count(char)
    if charCount >= min and charCount <=max:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
