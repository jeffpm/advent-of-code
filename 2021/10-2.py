import numpy as np
import statistics

def main():
    file = open('10-1.txt',mode='r')
    text = file.read()
    file.close()
    lines = text.splitlines()
    opened = []
    openers = "([{<"
    closers = ")]}>"
    incomplete = []
    # ( )
    # [ ]
    # { }
    # < >
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    total = 0
    for line in lines:
        corrupt = False
        # print(line)
        for c in line:
            # print(c)
            if c in openers:
                opened.append(c)
            elif c in closers:
                # print(opened)
                if opened[-1] == "(" and c != ")":
                    # print(f"expected ), found {c}")
                    # total += points[c]
                    corrupt = True
                    break
                elif opened[-1] == "(" and c == ")":
                    opened.pop()
                    continue
                
                if opened[-1] == "[" and c != "]":
                    # print(f"expected ], found {c}")
                    # total += points[c]
                    corrupt = True
                    break
                elif opened[-1] == "[" and c == "]":
                    opened.pop()
                    continue

                if opened[-1] == "{" and c != "}":
                    # print(f"expected }}, found {c}")
                    # total += points[c]
                    corrupt = True
                    break
                elif opened[-1] == "{" and c == "}":
                    opened.pop()
                    continue

                if opened[-1] == "<" and c != ">":
                    # print(f"expected >, found {c}")
                    # total += points[c]
                    corrupt = True
                    break
                elif opened[-1] == "<" and c == ">":
                    opened.pop()
                    continue
        if not corrupt:
            incomplete.append(line)
    scores = []
    
    for line in incomplete:
        total = 0 
        completer = ""
        opened = []
        for c in line:
            if c in openers:
                opened.append(c)
            elif c in closers:
                if opened[-1] == "(" and c == ")":
                    opened.pop()
                    continue
                elif opened[-1] == "{" and c == "}":
                    opened.pop()
                    continue
                elif opened[-1] == "[" and c == "]":
                    opened.pop()
                    continue
                elif opened[-1] == "<" and c == ">":
                    opened.pop()
                    continue
        for o in reversed(opened):
            if o == "(":
                completer += ")"
            elif o == "{":
                completer += "}"
            elif o == "[":
                completer += "]"
            elif o == "<":
                completer += ">"
        # print(completer)
        for c in completer:
            total = (total * 5) + points[c]
            # print(total)
        scores.append(total)
        # print(scores)
    scores.sort()
    print(scores)
    print(statistics.median(scores))

    # print(incomplete)
if __name__ == "__main__":
    main()