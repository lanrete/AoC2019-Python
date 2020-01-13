DATA_DIR = '../input'

with open(f'{DATA_DIR}/4', 'r') as f:
    _ = f.readline()
    start, end = [int(__) for __ in _.split('-')]


def check_valid_r1(n):
    have_double = False
    last_c = '-1'
    for c in str(n):
        if c == last_c:
            have_double = True
        if int(c) < int(last_c):
            return False
        last_c = c
    return have_double


def check_valid_r2(n):
    multi_digit = set()
    length = 1
    last_c = '-1'
    for ind, c in enumerate(str(n)):
        if c == last_c:
            length += 1
            if ind == 5:
                multi_digit.add(length)
        if (c != last_c) & (length != 1):
            multi_digit.add(length)
            length = 1
        if int(c) < int(last_c):
            return False
        last_c = c
    return 2 in multi_digit


def solve():
    ans1 = 0
    ans2 = 0
    for n in range(start, end):
        if check_valid_r1(n):
            ans1 += 1
        if check_valid_r2(n):
            ans2 += 1
    print(f'Answer to Q1: {ans1}')
    print(f'Answer to Q2: {ans2}')


get_answer = True
if get_answer:
    solve()
