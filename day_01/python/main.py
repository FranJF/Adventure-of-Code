def part_one(lines:list) -> tuple:

    almacen = []
    total_per_line:int = 0
    for line in lines:
        if line == "":
            almacen.append( total_per_line)
            total_per_line = 0
            continue
        total_per_line += int(line)

    highest = max(almacen)
    idx_highest = almacen.index(highest) + 1
    return almacen,idx_highest, highest

def part_two(almacen:list) -> tuple:
    almacen.sort(reverse=True)
    first_three = almacen[:3]
    suma = sum(first_three)
    return suma, first_three




def main():
    file = open("../input.txt", "r")
    lines = file.read().splitlines()
    file.close()

    almacen,_,_ = part_one(lines)
    return part_two(almacen)

print(main())
