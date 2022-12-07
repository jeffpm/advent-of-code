def main():
    total = 0
    file1 = open('3-1.txt', 'r')
    Lines = file1.readlines()
    pris = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    while count < len(Lines):
        l1 = (Lines[count].strip())
        l2 = (Lines[count+1].strip())
        l3 = (Lines[count+2].strip())
        for c in l1:
            if c in l2 and c in l3:
                total += pris.index(c) + 1
                break
        count += 3
    print(total)
if __name__ == "__main__":
    main()