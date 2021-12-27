import numpy as np


def main():
    file = open('10-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    opened = []
    openers = "([{<"
    closers = ")]}>"
    # ( )
    # [ ]
    # { }
    # < >

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    total = 0
    for line in lines:
        opened = []
        # print(line)
        for c in line:
            # print(c)
            if c in openers:
                opened.append(c)
            elif c in closers:
                # print(opened)
                if opened[-1] == "(" and c != ")":
                    print(f"expected ), found {c}")
                    total += points[c]
                    break
                elif opened[-1] == "(" and c == ")":
                    opened.pop()
                    continue
                
                if opened[-1] == "[" and c != "]":
                    print(f"expected ], found {c}")
                    total += points[c]
                    break
                elif opened[-1] == "[" and c == "]":
                    opened.pop()
                    continue

                if opened[-1] == "{" and c != "}":
                    print(f"expected }}, found {c}")
                    total += points[c]
                    break
                elif opened[-1] == "{" and c == "}":
                    opened.pop()
                    continue

                if opened[-1] == "<" and c != ">":
                    print(f"expected >, found {c}")
                    total += points[c]
                    break
                elif opened[-1] == "<" and c == ">":
                    opened.pop()
                    continue

    print(total)
if __name__ == "__main__":
    main()