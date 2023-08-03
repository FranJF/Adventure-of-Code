import string


def part_one(lineas: list, alphabet: list) -> int:
    points: int = 0
    for linea in lineas:
        firstString = linea[0:len(linea)//2]
        secondString = linea[len(linea)//2:]

        firstStringSet = set(firstString)
        secondStringSet = set(secondString)

        if not firstStringSet & secondStringSet:
            continue

        letter: str = (firstStringSet & secondStringSet).pop()
        point: int = alphabet.index(letter) + 1
        points += point

    return points


def part_two(lineas: list, alphabet: list) -> int:
    points: int = 0
    three_lines: list = []
    i: int = 0
    for linea in lineas:
        i += 1
        three_lines.append(linea)
        if (i == 3):
            letter: str = (set(three_lines[0]) & set(
                three_lines[1]) & set(three_lines[2])).pop()
            point: int = alphabet.index(letter) + 1
            points += point
            three_lines = []
            i = 0

    return points


def main():
    archivo = open("../input.txt", "r")
    lineas = archivo.read().splitlines()
    archivo.close()

    alphabet: list = list(string.ascii_letters)
    return part_one(lineas, alphabet), part_two(lineas, alphabet)


if __name__ == "__main__":
    print(main())
