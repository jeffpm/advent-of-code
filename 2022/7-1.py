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
    tempSize = 0
    global sizes
    daSize += node.size
    print(f'made it to: {node}')
    if len(node.children) == 0:
        print('returning size')
        print(f'daSize: {daSize}')
        return daSize
    else:
        #node.showChildren()
        tempSize += daSize
        daSize = 0
        for c in node.children:
            print(f'exploring {c}')
            daSize = getSize(c, daSize)
            sizes[node.data] = daSize
            tempSize += daSize
        sizes[node.data] = daSize
        return tempSize
def main():
    root = Tree("/")
    curr = None
    file1 = open('7-test.txt', 'r')
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
    print(daNode)
    daNode.showChildren()
    print(getSize(daNode))
    print(sizes)
    daSum = 0
    for key, val in sizes.items():
        if val <=100000:
            daSum += val

    print(daSum)
if __name__ == "__main__":
    main()
