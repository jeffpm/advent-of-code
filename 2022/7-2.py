class Tree:
    def __init__(self, data, parent = None, size = 0):
        self.children = []
        self.data = data
        self.parent = parent
        self.size = size
    def __str__(self):
        return f'data: {self.data}, size: {self.size}'
    def showChildren(self):
        print(f'{self.data}\'s children:')
        for c in self.children:
            print(c)
            #continue

sizes = dict()
def getSize(node, daSize = 0):
    # if a directory, iterate through
    if node.size == 0:
        daSize = 0
        for c in node.children:
            daSize += getSize(c, daSize)
        sizes[node.data] = daSize
        return 0
    else:
        return node.size
    # if a file, return size
def main():
    root = Tree("/")
    curr = None
    file1 = open('7-1.txt', 'r')
    Lines = file1.readlines()

    for l in Lines:
        l = l.strip()
        #print(l)
        l2 = l.split(" ")
        if l2[0] == '$':
            if l2[1] == 'cd':
                #print(f'changed dir: {curr}')
                if l2[2] == '/':
                    curr = root
                elif l2[2] == '..':
                    curr = curr.parent
                else:
                    child = l2[2]
                    for c in curr.children:
                        if c.data.endswith(child):
                            curr = c
                            break
            # elif l2[1] == 'ls':
            #     print()
        else:
            newpath = curr.data
            if not newpath.endswith('/'):
                newpath += '/'
            if l2[0] == "dir":
                temp = Tree(newpath + l2[1], curr)
                #print(f'adding: {temp}')
                curr.children.append(temp)
            else:
                size = int(l2[0])
                temp = Tree(newpath + l2[1], curr, size)
                #print(f'adding: {temp}')
                curr.children.append(temp)

    daNode = root
    # print(daNode)
    # daNode.showChildren()
    getSize(daNode)
    #print(sizes)
    finder = "/"
    total = 0
    daSum = 0
    totalSizes = dict()
    for key, val in sizes.items():
        totalSizes[key] = val
        for key2, val2, in sizes.items():
            if key2 != key:
                if key2.startswith(key):
                    totalSizes[key] += val2
    print (totalSizes)
    totalSizes = dict(sorted(totalSizes.items(), key=lambda item: item[1]))
    print (totalSizes)
    totalSpace = 70000000
    updateAmountNeeded = 30000000
    unusedSpace = totalSpace - totalSizes['/']
    #print(unusedSpace)

    for key, val in totalSizes.items():
        if val + unusedSpace >= updateAmountNeeded:
            print(val)
            break
    #     if val <=100000:
    #         daSum += val

    # print(daSum)
if __name__ == "__main__":
    main()
