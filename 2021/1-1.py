def main():
    mes = []
    prev = -1
    increaseCounter = 0
    f = open("1-1.txt", "r")
    for x in f:
        if prev != -1:
            if int(x) > int(prev):
                increaseCounter += 1
        prev = int(x)

    print (increaseCounter)
if __name__ == "__main__":
    main()