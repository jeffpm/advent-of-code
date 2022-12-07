def main():
    with open('9-1.txt') as f:
        lines = f.read().splitlines()

    preamble = 25
    for counter, line in enumerate(lines):
        # print(counter)
        if counter >= preamble:
            nums = lines[counter - preamble: counter]
            valid = False
            for xc, x in enumerate(nums):
                for yc, y in enumerate(nums):
                    if xc != yc:
                        if int(x) + int(y) == int(line):
                            valid = True
                            break
                if valid:
                    break
            if not valid:
                print(f"value {line} is a bad boi")
                break
if __name__ == "__main__":
    main()
