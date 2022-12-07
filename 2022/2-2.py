def main():
    file1 = open('2-1.txt', 'r')
    Lines = file1.readlines()

    total = 0 

    for l in Lines:
        l = l.strip()

        i = l.split(" ")
        i1 = i[0]
        i2 = i[1]
        if i2 == "X":
            if i1 == "A":
                i2 = "Z"
            elif i1 == "B":
                i2 = "X"
            else:
                i2 = "Y"
        elif i2 == "Y":
            total += 3
            if i1 == "A":
                i2 = "X"
            elif i1 == "B":
                i2 = "Y"
            else:
                i2 = "Z"
        elif i2 == "Z":
            total += 6
            if i1 == "A":
                i2 = "Y"
            elif i1 == "B":
                i2 = "Z"
            else:
                i2 = "X"

        if i2 == "X":
            total += 1
        elif i2 == "Y":
            total += 2
        elif i2 == "Z":
            total += 3
    print(total)

if __name__ == "__main__":
    main()