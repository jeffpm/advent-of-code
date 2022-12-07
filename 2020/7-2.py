matches = set()
daSum = 0
def main():
    with open('7-1.txt') as f:
        lines = f.read().splitlines()

        deps = {}

    for line in lines:
        firstSplit = line.split(" contain ")
        parent = firstSplit[0].split(" ")[0] + " " + firstSplit[0].split(" ")[1]
        temp = {}
        children = firstSplit[1].split(", ")
        for child in children:
            if "no other bags" not in child:
                temp[child.split(" ")[1] + " " + child.split(" ")[2]] = int(child.split(" ")[0])
        deps[parent] = temp

    answer = set()
    
    def getSum(color):
        global daSum
        for dep in deps[color]:
            daSum += deps[color][dep]
            for _ in range(0, deps[color][dep]):
                getSum(dep)

    getSum("shiny gold")
    print(daSum)

if __name__ == "__main__":
    main()
