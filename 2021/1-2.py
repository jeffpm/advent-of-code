def main():
    lines = []
    f = open("1-1.txt", "r")
    prev = -1
    increaseCounter = 0
    for x in f:
        lines.append(int(x))

    for count, x in enumerate(lines):
        try:
            sum = lines[count] + lines[count + 1] + lines [count + 2]
            print(sum)
            if prev != -1:
                if sum > prev:
                    increaseCounter += 1
            prev = sum
            
        except:
            continue

    print(increaseCounter)

if __name__ == "__main__":
    main()