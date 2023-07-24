MOVEMENTS = {
    "X": "A",
    "Y": "B",
    "Z": "C",
    "A": "X",
    "B": "Y",
    "C": "Z",
}
POINTS_PER_MOVE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
COMBINATIONS = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "X": "C",
    "Y": "A",
    "Z": "B",
}
COMBINATIONS_TODO = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

def read():
    file = open("../input.txt", "r")
    lines = file.readlines()
    file.close()
    return lines


def get_points(move1, my_move):
    points:int = 0
    if move1 == COMBINATIONS[my_move]:
        points += 6
    elif move1 == MOVEMENTS[my_move]:
        points += 3
    else:
        points += 0
    return points


def part_one(lines):
    points = 0
    for line in lines:
        line = line.strip()
        move1, my_move = line.split(" ")
        points += get_points(move1, my_move)
        points += POINTS_PER_MOVE[my_move]

    return points

def part_two(lines):
    points = 0
    for line in lines:
        line:str = line.strip()
        move1, my_move = line.split(" ")

        todo:int = COMBINATIONS_TODO[my_move]
        if todo == 0:
            my_move = COMBINATIONS[move1]
        elif todo == 3:
            my_move = MOVEMENTS[move1]
        elif todo == 6:
            for key, value in COMBINATIONS.items():
                if value == move1:
                    my_move = key
        else:
            raise Exception("Unknown todo")

        points += todo
        points += POINTS_PER_MOVE[my_move]

    return points

def main():
    lines = read()
    return part_one(lines), part_two(lines)

print(main())
