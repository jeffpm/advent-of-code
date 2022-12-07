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
            total += 1
        elif i2 == "Y":
            total += 2
        elif i2 == "Z":
            total += 3
            
        if (i1 == "A" and i2 == "X") or (i1 == "B" and i2 == "Y") or (i1 == "C" and i2 == "Z"):
            total += 3
            continue

        elif i1 == "A":
            if i2 == "Y":
                total += 6
            continue

        elif i1 == "B":
            if i2 == "Z":
                total += 6
            continue

        elif i1 == "C":
            if i2 == "X":
                total += 6
            continue
    print(total)

if __name__ == "__main__":
    main()