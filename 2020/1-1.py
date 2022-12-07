def main():
    nums = []
    f = open("1-1.txt", "r")
    for x in f:
        nums.append(int(x))
    for count1, x in enumerate(nums):
        for count2, y in enumerate(nums):
            if count1 == count2:
                continue

            if x + y == 2020:
                print(x*y)
                return
if __name__ == "__main__":
    main()
