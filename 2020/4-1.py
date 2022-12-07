def main():
    with open('4-1.txt') as f:
        lines = f.read().splitlines()

    reqFields = [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ]
    keys = []
    count = 0
    for linecount, x in enumerate(lines):
        pairs = x.split(" ")
        for pair in pairs:
            keys.append(pair.split(":")[0])

        if x=="" or linecount==len(lines)-1:
            valid = True
            for field in reqFields:
                if field not in keys:
                    valid = False
            if valid:
                count += 1
            keys = []
    print(count)
if __name__ == "__main__":
    main()
