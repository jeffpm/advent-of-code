
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

    maxScore = 0
    for row, x in enumerate(trees):
        for col, val in enumerate(x):
            if not (row == 0 or row == size - 1 or col == 0 or col == size - 1):
                score = 1
                for t in [trees[row][0:col][::-1], trees[row][col+1:size], trees[:,col][0:row][::-1], trees[:,col][row+1:size]]:
                    for count, height in enumerate(t):
                        counter = count + 1
                        if height >= val:
                            break
                    score *= counter
                if score > maxScore:
                    maxScore = score
            
    print(f'answer: {maxScore}')
    
if __name__ == "__main__":
    main()
