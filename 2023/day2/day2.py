# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2

def day2():
    red = 12
    green = 13
    blue = 14

    res = 0

    puzzle_input = open("2023\day2\input.txt", "r")
    for id, line in enumerate(puzzle_input):

        sets = line[7+ len(str(id)):].split("; ")
        is_valid = True

        for set in sets:
            r, g, b = 0, 0, 0

            l = set.split(", ")
            
            for item in l:
                pair = item.strip().split(' ')
                colour = pair[1]
                val = int(pair[0])

                if colour == 'red':
                    r += val
                elif colour == 'green':
                    g += val
                elif colour == 'blue':
                    b += val

            if r > red or g > green or b > blue:
                is_valid = False
                break
            
        if is_valid:
            res += (id + 1)

    return res     


if __name__ == "__main__":
    print(day2())
