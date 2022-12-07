matches = set()
def main():
    with open('7-1.txt') as f:
        lines = f.read().splitlines()

        deps = {}

    for line in lines:
        firstSplit = line.split(" contain ")
        parent = firstSplit[0].split(" ")[0] + " " + firstSplit[0].split(" ")[1]
        # print(parent)
        temp = []
        children = firstSplit[1].split(", ")
        for child in children:
            if "no other bags" not in child:
                temper = child.split(" ")[1] + " " + child.split(" ")[2]
                temp.append(temper)
        deps[parent] = temp
    print(deps)
    answer = set()
    def doesContain(color):
        for dep in deps:
            print(f"working {dep}")
            if color in deps[dep]:
                answer.add(dep)
                print(f"calling doescontain with {dep}")
                doesContain(dep)
    doesContain("shiny gold")
    print(len(answer))



    
if __name__ == "__main__":
    main()
