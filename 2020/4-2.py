import re

def main():
    with open('4-1.txt') as f:
        lines = f.read().splitlines()

    reqFields = [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ]
    keys = []
    count = 0
    total = 0
    tempPairs = []
    for linecount, x in enumerate(lines):
        pairs = x.split(" ")
        for pair in pairs:
            if pair != "":
                keys.append(pair.split(":")[0])
                tempPairs.append((pair.split(":")[0], pair.split(":")[1]))
                # print(pair)
                # print(validate(pair.split(":")[0], pair.split(":")[1]))

        if x=="" or linecount==len(lines)-1:
            valid = True
            fieldsValid = True
            for field in reqFields:
                if field not in keys:
                    valid = False
            for pair in tempPairs:
                # print(pair)
                # print(validate(pair[0], pair[1]))
                if not validate(pair[0], pair[1]):
                    fieldsValid = False
                    break
            if valid and fieldsValid:
                # print(f"VALID: {tempPairs}")
                count += 1
            total += 1
            keys = []
            tempPairs = []
    print(count)
    print(f"total: {total}")

def validate(key, value):
    if key == "byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002
    elif key == "iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020
    elif key == "eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030
    elif key == "hgt":
        if value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        else: 
            print(value[-2:])
            return False
    elif key == "hcl":
        return re.match("#[a-f|0-9]{6}", value) is not None and len(value) == 7
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and len(value) == 3
    elif key == "pid":
        return re.match("[0-9]{9}", value) is not None and len(value) == 9
    return True 

if __name__ == "__main__":
    main()
