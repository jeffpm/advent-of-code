def main():
    file = open('6-1.txt',mode='r')
    text = file.read()
    file.close()

    count = 0
    groups = text.split("\n\n")
    for group in groups:
        total = set()
        people = group.split("\n")
        for person in people:
            for answers in person:
                for answer in answers:
                    if (all([answer in person for person in people])):
                        total.add(answer)
        count += len(total)
    print(count)

if __name__ == "__main__":
    main()