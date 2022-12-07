with open('01.txt') as f:
    line = f.readline()
    floor = 0
    for count, c in enumerate(line):
        floor = floor + 1 if c == '(' else floor - 1
    print(floor)
    floor = 0
    for count, c in enumerate(line):
        floor = floor + 1 if c == '(' else floor - 1
        print(f'{c}, {floor}, {count + 1}')
        if floor == -1:
            print(count + 1)
            break

    