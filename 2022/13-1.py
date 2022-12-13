def convert(input, level = 0):
    startChar = ""
    tempList = list()
    stack = list()
    startPos = list()
    for x, c in enumerate(input):
        # print(c)
        if c == '[':
            print(f'level: {level} - adding [ to stack: {stack}')
            stack.append('[')
            if len(stack) > 1:
                startPos.append(x)
                startChar = x
                print(f'startChar: {x}')
        elif c == ']':
            if len(stack) == 1 and stack[-1] == '[':
                print(f'level: {level} - finished with list: {tempList}')
                #print(f'{x}')
                if not (level == 0 and x != len(input) - 1):
                    return tempList
            else:
                # print(f'input: {input}')
                print(f'startChar: {startChar}')
                print(f'level: {level} - trying to add {input[startChar:x+1]}')
                tempList.append(convert(input[startChar:x+1], level + 1))
                stack.pop(-1)
                startChar = ""
        elif c == ',':
            pass
        else:
            if startChar == "":
                
                # if isinstance(c, list):
                #     tempList.append(c)
                # else:
                print(f'level: {level} - appending: {c}')
                tempList.append(int(c))
                # print(f'result: {tempList}')
                # print(x)
def main():
    # file1 = open('13-test.txt', 'r')
    # Lines = file1.readlines()
    # for line in Lines:
    #     line = line.strip()
    #     convert(line)

    assert len(convert('[]')) == 0
    assert convert('[3]')[0] == 3
    assert convert('[7,7,7]')[0] == 7 and convert('[7,7,7]')[1] == 7 and convert('[7,7,7]')[2] == 7
    assert isinstance(convert('[[8,7,6]]')[0], list) and len(convert('[[8,7,6]]')[0]) == 3
    assert len(convert('[[]]')) == 1 and convert('[[]]')[0] == []
    assert len(convert('[[1],[2,3,4]]')) == 2 and convert('[[1],[2,3,4]]')[0][0] == 1 and convert('[[1],[2,3,4]]')[1] == [2,3,4]
    assert len(convert('[[4,4],4,4]')) == 3 and convert('[[4,4],4,4]')[0] == [4,4] and convert('[[4,4],4,4]')[1] == 4
    assert len(convert('[[1],4]')) == 2 and convert('[[1],4]')[0] == [1] and convert('[[1],4]')[1] == 4
    # print(convert('[[[]]]'))
    # print(convert('[1,[2,[3,[4,[5,6,7]]]],8,9]'))

    # assert len(convert('[[[]]]')) == 1
   
    
if __name__ == "__main__":
    main()