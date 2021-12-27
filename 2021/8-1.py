def main():
    file = open('8-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()

    matches = [2, 3, 4, 7]
    counter = 0
    for line in lines:
        outputs = line.split(" | ")[1].split(" ")

        for output in outputs:
            if len(output) in matches:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()