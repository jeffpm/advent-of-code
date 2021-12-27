from time import perf_counter
def main():
    daList = []
    daDict = {0:(),6:(),1:(),7:(),2:(),19:(),20:()}
    turnCount = 30000000
    startCount = len(daDict)

    for count, x in enumerate(daDict.keys()):
        daDict[x] = (count + 1, -1)
        lastNum = x

    for count in range(len(daDict), turnCount):
        if daDict[lastNum][1] != -1:
            lastNum = daDict[lastNum][1] - daDict[lastNum][0]
        else:
            lastNum = 0
        speak(daDict, lastNum, count + 1)

    print(lastNum)

def speak(daDict, lastNum, count):
    if lastNum not in daDict.keys():
        daDict[lastNum] = (count, -1)
    elif daDict[lastNum][1] == -1:
        temp = daDict[lastNum]
        daDict[lastNum] = (temp[0], count)
    else:
        temp = daDict[lastNum]
        daDict[lastNum] = (temp[1], count)
    
    return daDict

if __name__ == "__main__":
    t1_start = perf_counter() 
    main()
    t1_stop = perf_counter() 
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start) 