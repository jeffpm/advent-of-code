
import numpy as np
def main():
    file1 = open('8-1.txt', 'r')
    Lines = file1.readlines()

    size = len(Lines)
    trees = np.zeros((size, size), int)

    for r, l in enumerate(Lines):
        l = l.strip()
        for c, x in enumerate(l):
            trees[r][c] = int(x)

    numVisible = 2 * size + 2 * (size - 2)
    for row, x in enumerate(trees):
        for col, val in enumerate(x):
            if not (row == 0 or row == size - 1 or col == 0 or col == size - 1):
                for t in [trees[row][0:col], trees[row][col+1:size], trees[:,col][0:row], trees[:,col][row+1:size]]:
                    if not any(z >= val for z in t):
                        numVisible += 1
                        break           
    print(f'answer: {numVisible}')
if __name__ == "__main__":
    main()
