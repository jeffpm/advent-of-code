from collections import defaultdict
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


# def getSize(node, daSize = 0):
#     # if a directory, iterate through
#     if node.size == 0:
#         daSize = 0
#         for c in node.children:
#             daSize += getSize(c, daSize)
#         sizes[node.data] = daSize
#         return 0
#     else:
#         return node.size
#     # if a file, return size
def main():
    sizes = defaultdict(int)
    root = Tree("/")
    curr = None
    file1 = open('7-1.txt', 'r')
    Lines = file1.readlines()

    for l in Lines:
        l = l.strip()
        l2 = l.split(" ")
        if l2[0] == '$':
            if l2[1] == 'cd':
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
        else:
            newpath = curr.data
            if not newpath.endswith('/'):
                newpath += '/'
            if l2[0] == "dir":
                temp = Tree(newpath + l2[1], curr)
                curr.children.append(temp)
            else:
                size = int(l2[0])
                sizes[curr.data] += size
                temp = Tree(newpath + l2[1], curr, size)
                curr.children.append(temp)
    # print(sizes)
    sizes = dict(sorted(sizes.items()))
    print(sizes)
    total = 0
    for key, val in sizes.items():
        for key2, val2 in sizes.items():
            if key2 != key:
                if key2.startswith(key):
                    sizes[key] += val2
    for key, val in sizes.items():
        if val <= 100000:
            total += val
    print(sizes)
    print(total)
if __name__ == "__main__":
    main()
