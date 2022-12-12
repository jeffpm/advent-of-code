global monkeys
monkeys = list()

class Monkey:
    def __init__(self):
        self.items = list()
        self.operator = ""
        self.amount = 0
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspectTotal = 0

    def addItem(self, item):
        self.items.append(item)
    
    def setOperator(self, operation):
        match operation.split():
            case ['new', '=', x, operator, amount]:
                self.operator = operator
                self.amount = amount

    def setTest(self, test):
        self.test = int(test)

    def setTrue(self, true):
        self.true = true

    def setFalse(self, false):
        self.false = false
    
    def inspectItems(self):
        for item in self.items:
            self.inspectTotal += 1
            if self.amount == "old":
                tempAmount = item
            else:
                tempAmount = int(self.amount)
            if self.operator == "+":
                worry = item + tempAmount
            elif self.operator == "*":
                worry = item * tempAmount
            
            worry = int(worry / 3)
            if worry % self.test == 0:
                monkeys[self.true].addItem(worry)
            else:
                monkeys[self.false].addItem(worry)
            self.items = []


def main():
    global monkeys
    for line in open('11-1.txt'):
        match line.strip().split():
            case ["Monkey", *objects]:
                monkey = Monkey()
            case ["Starting", *objects]:
                l2 = line.split(":")
                l3 = l2[1].split(",")
                for item in l3:
                    monkey.addItem(int(item))
            case ["Operation:", *objects]:
                l2 = line.split(":")
                monkey.setOperator(l2[1].strip())
            case ["Test:", *objects]:
                monkey.setTest(int(line.split()[-1]))
            case ["If", "true:", *objects]:
                monkey.setTrue(int(line.split()[-1]))
            case ["If", "false:", *objects]:
                monkey.setFalse(int(line.split()[-1]))
                monkeys.append(monkey)

    for x in range(0, 20):
        for monkey in monkeys:
            monkey.inspectItems()

    totals = list()
    for monkey in monkeys:
        totals.append(monkey.inspectTotal)
    totals.sort(reverse=True)
    print(totals[0] * totals[1])

if __name__ == "__main__":
    main()