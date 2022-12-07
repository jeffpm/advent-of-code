with open('02.txt') as f:
    presents = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
presents = [x.strip().split('x') for x in presents]
# print(presents)
answer = 0
for present in presents:
    l, w, h = [int(x) for x in present]
    answer += (2 * l * w) + (2 * w * h )+ (2 * h *l) + min([l * w, w * h, h * l])
print(answer)

answer = 0
for present in presents:
    l, w, h = [int(x) for x in present]
    answer += 2 * min([l + w, w + h, h + l]) + (l * w * h)
print(answer)