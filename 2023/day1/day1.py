# Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1

def day1():
    # Import text file
    puzzle_input = open("input.txt", "r")
    res = 0

    # Itreate through each line
    for line in puzzle_input:
        n = []

        # Add all numbers to array
        for char in line:
            if char.isdigit(): n.append(char)
        
        if len(n) == 0: continue
        else: res += int( n[0] + n[-1] )
        print(n, int( n[0] + n[-1] ))

    return res

if __name__ == "__main__":
    print(day1())