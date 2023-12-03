import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


f = open('day2-input.txt', 'r')
lines = f.readlines()
f.close()

result = 0
set_power = 0
for line in lines:
    gid = re.search('^Game (\d+):', line)
    blues = max([int(m) for m in re.findall('(\d+) blue', line)])
    greens = max([int(m) for m in re.findall('(\d+) green', line)])
    reds = max([int(m) for m in re.findall('(\d+) red', line)])
    if blues <= MAX_BLUE and greens <= MAX_GREEN and reds <= MAX_RED:
        result += int(gid.group(1))
    set_power += blues * greens * reds

print('Part 1: %d' % result)
print('Part 2: %d' % set_power)
