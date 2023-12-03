import re

SYMBOL = re.compile('[^.0-9]')

def search_around_digit(lines, y, x):
    is_part = False
    gear_coord = None
    
    # check left of digit
    if x > 0 and re.match(SYMBOL, lines[y][x-1]):
        is_part = True
        if lines[y][x-1] == '*':
            gear_coord = (x-1, y)
    # check right of digit
    if x < len(lines[y]) - 1 and re.match(SYMBOL, lines[y][x+1]):
        is_part = True
        if lines[y][x+1] == '*':
            gear_coord = (x+1, y)
    # check diagonally to the left above digit
    if x > 0 and y > 0 and re.match(SYMBOL, lines[y-1][x-1]):
        is_part = True
        if lines[y-1][x-1] == '*':
            gear_coord = (x-1, y-1)
    # check diagonally to the right above digit
    if x < len(lines[y]) - 1 and y > 0 and re.match(SYMBOL, lines[y-1][x+1]):
        is_part = True
        if lines[y-1][x+1] == '*':
            gear_coord = (x+1, y-1)
    # check above digit
    if y > 0 and re.match(SYMBOL, lines[y-1][x]):
        is_part = True
        if lines[y-1][x] == '*':
            gear_coord = (x, y-1)
    # check diagonally to the left below digit
    if x > 0 and y < len(lines) - 1 and re.match(SYMBOL, lines[y+1][x-1]):
        is_part = True
        if lines[y+1][x-1] == '*':
            gear_coord = (x-1, y+1)
    # check diagonally to the right below digit
    if x < len(lines[y]) - 1 and y < len(lines) - 1 and re.match(SYMBOL, lines[y+1][x+1]):
        is_part = True
        if lines[y+1][x+1] == '*':
            gear_coord = (x+1, y+1)
    # check below digit
    if y < len(lines) - 1 and re.match(SYMBOL, lines[y+1][x]):
        is_part = True
        if lines[y+1][x] == '*':
            gear_coord = (x, y+1)

    return (is_part, gear_coord)


f = open('day3-input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

gear_adj_map = {}

parts = []
for line_num, line in enumerate(lines):
    # get all numbers within the current line
    numbers_in_line = re.finditer('\d+', line)
    # for each number, look for a symbol above/below/left/right of each individual digit
    for n in numbers_in_line:
        for i in range(n.start(), n.end()):
            is_part, found_gear = search_around_digit(lines, line_num, i)
            if is_part:
                parts.append(int(n.group(0)))
                if found_gear:
                    val = gear_adj_map.get(found_gear)
                    if val is not None:
                        val.get('parts').append(int(n.group(0)))
                        gear_adj_map[found_gear] = { 'count': val.get('count') + 1, 'parts': val.get('parts') }
                    else:
                        gear_adj_map[found_gear] = { 'count': 1, 'parts': [int(n.group(0))] }
                break

ratio_sum = 0
for key, val in gear_adj_map.items():
    if val.get('count') == 2:
        ratio_sum += val.get('parts')[0] * val.get('parts')[1]
        

print('Part 1: %d' % sum(parts))
print('Part 2: %d' % ratio_sum)
