def check(cycle, x, total):
    checks = [20, 60, 100, 140, 180, 220]
    if cycle in checks:
        total += (cycle * x)
    return total

def main():
    x = 1
    cycle = 0
    total = 0
    
    for line in open('10-1.txt'):
        cycle += 1
        total = check(cycle, x, total)
        match line.split():
            case ["noop"]:
                pass
            case ["addx", step]:
                cycle += 1
                total = check(cycle, x, total)
                x += int(step)

    print(total)

if __name__ == "__main__":
    main()