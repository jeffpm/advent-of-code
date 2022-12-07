import numpy as np
def main():
    with open('3-1.txt') as f:
        lines = f.read().splitlines()
    data = np.empty((len(lines), len(lines[0])), dtype=str)
    
    for rcount, row in enumerate(lines):
        for ccount, col in enumerate(row):
            data[rcount][ccount] = col
    moves = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    
    answers = []
    total = 0
    for move in moves:
        rMov = move[0]
        cMov = move[1]

        r = 0
        c = 0
        numTrees = 0
        done = False
        while not done:
            if r >= len(data):
                done = True
                break
            if data[r][c] == '#':
                numTrees += 1

            if c + cMov >= len(data[0]):
                c = (c + cMov) % len(data[0])
            else:
                c = c + cMov
            
            r = r + rMov
        answers.append(numTrees)
    for a in answers:
        if total == 0:
            total = a
        else:
            total *= a
    print(total)


if __name__ == "__main__":
    main()
