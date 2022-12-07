def main():
    total = 0
    file1 = open('3-1.txt', 'r')
    Lines = file1.readlines()
    pris = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0 

    for l in Lines:
        l = l.strip()
        l1 = l[0:int(len(l)/2)]
        l2 = l[int(len(l)/2):]
        for c in l1:
            if c in l2:
                total += pris.index(c) + 1
                break
    print(total)
if __name__ == "__main__":
    main()