def main():
    file1 = open('4-1.txt', 'r')
    Lines = file1.readlines()
    total = 0 

    for l in Lines:
        l = l.strip()
        l = l.split(",")
        e1 = l[0]
        e2 = l[1]
        e1s = int(e1.split("-")[0])
        e1e = int(e1.split("-")[1])
        e2s = int(e2.split("-")[0])
        e2e = int(e2.split("-")[1])

        for x in range(e1s, e1e+1):
            if x >= e2s and x <= e2e:
                total += 1
                break
        # if e1s >= e2s and e1e <= e2e:
        #     total += 1
        # elif e2s >= e1s and e2e <= e1e:
        #     total += 1

    print(total)
if __name__ == "__main__":
    main()