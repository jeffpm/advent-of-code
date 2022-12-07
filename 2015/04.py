import hashlib

counter = 0
theInput = "ckczppom"
while(True):
    doIt = theInput + str(counter)
    result = hashlib.md5(doIt.encode())
    result = result.hexdigest()
    # print(str(result))
    if str(result)[0:5] == "00000":
        print(counter)
    if str(result)[0:6] == "000000":
        print(counter)
        break
    counter += 1