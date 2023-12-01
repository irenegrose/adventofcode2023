import re

def rev(s):
    return ''.join(reversed(list(s)))

DIGITS = [str(d) for d in range(10)]
NUMBER_STR = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
NUMBER_STR_REV = [rev(d) for d in NUMBER_STR]

def to_num(m):
    s = m.group()
    for idx, val in enumerate(NUMBER_STR):
        s = s.replace(val, DIGITS[idx])
    return s


def to_num_rev(m):
    s = m.group()
    for idx, val in enumerate(NUMBER_STR):
        s = s.replace(rev(val), DIGITS[idx])
    return s


input_file = open('day1-input.txt', 'r')
output_file = open('day1-output.txt', 'w')
lines = input_file.readlines()

result = 0
for l in lines:
    cur = ''
    first_dig = re.sub('|'.join(NUMBER_STR), to_num, l, count=1)
    chrs = [n for n in list(first_dig) if n in DIGITS]
    cur += chrs[0]

    last_dig = re.sub('|'.join(NUMBER_STR_REV), to_num_rev, rev(l), count=1)
    chrs = [n for n in list(last_dig) if n in DIGITS]
    cur += chrs[0]
    
    result += int(cur)
    output_file.write(l.strip() + ' --> ' + cur + '\n')
    
print(result)
input_file.close()
output_file.close()
