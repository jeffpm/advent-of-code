def main():
    # fishes = []
    # f = open("6-1.txt", "r")
    # for x in f:
    #     fishes = [int(fish) for fish in x.split(',')]

    # days = 256

    # for d in range (1, 80):
    fishes = []
    f = open("6-1.txt", "r")
    for x in f:
        fishes = [int(fish) for fish in x.split(',')]
    for x in range(0, 256):
        newFishes = []
        for index, fish in enumerate(fishes):
            if fish > 0:
                fishes[index] = fish -1
            else:
                newFishes.append(8)
                fishes[index] = 6

        fishes.extend(newFishes)
        print(f"day: {x + 1} fish: {len(fishes)}")
if __name__ == "__main__":
    main()