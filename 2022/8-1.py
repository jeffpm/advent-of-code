
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
                left = trees[row][0:col]
                if not any(z >= val for z in left):
                    numVisible += 1
                    continue
                right = trees[row][col+1:size]
                if not any(z >= val for z in right):
                    numVisible += 1
                    continue
                up = trees[:,col][0:row]
                if not any(z >= val for z in up):
                    numVisible += 1
                    continue
                down = trees[:,col][row+1:size]
                if not any(z >= val for z in down):
                    numVisible += 1
                    continue
           
    print(f'answer: {numVisible}')
if __name__ == "__main__":
    main()
