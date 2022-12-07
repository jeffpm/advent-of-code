operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']
signals = {}
operations = {}

def isInt(val):
    try:
        int(val)
        return True
    except:
        return False

def processVals(val):
    if len(val)>1:
        try:
            val1 = int(val[1])
        except:
            val1 = signals[val[1]]
    if len(val) > 2:
        try:
            val2 = int(val[2])
        except:
            val2 = signals[val[2]]

def processOp(signals, val):
    answer = None
    val1 = None
    val2 = None

    if val[0] in ('AND', 'OR'):
        if (val[1] in signals.keys() or isInt(val[1])) and (val[2] in signals.keys() or isInt(val[2])):
            if len(val)>1:
                try:
                    val1 = int(val[1])
                except:
                    val1 = signals[val[1]]
            if len(val) > 2:
                try:
                    val2 = int(val[2])
                except:
                    val2 = signals[val[2]]
            if val[0] == 'AND':
                # print('made it1')
                answer = val1 & val2
            else:
                # print('made it2')
                answer = val1 | val2
        else:
            answer = None
    elif val[0] in ('LSHIFT', 'RSHIFT'):
        if val[1] in signals.keys() or isInt(val[1]):
            if len(val)>1:
                try:
                    val1 = int(val[1])
                except:
                    val1 = signals[val[1]]
            if len(val) > 2:
                try:
                    val2 = int(val[2])
                except:
                    val2 = signals[val[2]]
            if val[0] == 'LSHIFT':
                # print('made it3')
                answer = val1 << int(val2)
                # print(answer)
            else:
                # print('made it4')
                answer = val1 >> int(val2)
        else:
            answer = None
    elif val[0] == 'NOT':
        if val[1] in signals.keys():
            if len(val)>1:
                try:
                    val1 = int(val[1])
                except:
                    val1 = signals[val[1]]
            if len(val) > 2:
                try:
                    val2 = int(val[2])
                except:
                    val2 = signals[val[2]]
            # print('made it5')
            answer = 65535 - int(val1)
        else:
            answer = None
    elif len(val) == 1:
        if val[0] in signals.keys():
            # print('made it6')
            answer = signals[val[0]]
        else:
            answer = None
    return answer

with open('07.txt') as f:
    insts = [line.rstrip() for line in f.readlines()]
for inst in insts:
    ins, outs = [x.strip() for x in inst.split('->')]
    # print(f'{ins},{outs}')
    if any(op in ins for op in operators):
        if len(ins.split(' ')) == 2:
            operations[outs] = [ins.split(' ')[0], ins.split(' ')[1]]

        elif len(ins.split(' ')) == 3:
            operations[outs] = [ins.split(' ')[1], ins.split(' ')[0], ins.split(' ')[2]]
        
    else:
        try:
            # print(ins)
            signals[outs] = int(ins)
        except:
            # print(f'added {ins}')
            operations[outs] = [ins]
deleteList = []
while len(operations) > 0:
    for t in deleteList:
        operations.pop(t)
    deleteList = []
    for key, val in operations.items():
        result = processOp(signals, val)
        if result is not None:
            signals[key] = result
            deleteList.append(key)
# print(signals)
print(signals['a'])

