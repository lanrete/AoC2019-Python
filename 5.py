DATA_DIR = '../input'

with open(f'{DATA_DIR}/5', 'r') as f:
    raw = f.readline()
    codes = [int(_) for _ in raw.split(',')]
    print(f'{len(codes)} op codes found')


def get_mode(instruction):
    opcode = instruction % 100
    m1 = (instruction % 1000) // 100
    m2 = (instruction % 10000) // 1000
    m3 = instruction // 10000
    return opcode, m1, m2, m3


def get(codes, pos):
    if pos >= len(codes):
        return 'Invalid'
    return codes[pos]


def get_status(op, p1, p2, p3):
    s = f'{op}'
    for p in [p1, p2, p3]:
        if p != 'Invalid':
            s += f' {p}'
    print(s)


def intcode_computer(inp, codes):
    ind = 0
    inc_dict = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}
    opcode, m1, m2, m3 = get_mode(codes[ind])
    while opcode != 99:
        p1 = get(codes, ind + 1)
        p2 = get(codes, ind + 2)
        p3 = get(codes, ind + 3)
        get_status(opcode, p1, p2, p3)

        inc = inc_dict.get(opcode, 0)
        if opcode == 1:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'Adding {p1} and {p2} and putting the result into {p3}')
            codes[p3] = p1 + p2
        if opcode == 2:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'Multiplying {p1} and {p2} and putting the result into {p3}')
            codes[p3] = p1 * p2
        if opcode == 3:
            print(f'Putting {inp} into position {p1}')
            codes[p1] = inp
        if opcode == 4:
            p1 = codes[p1] if m1 == 0 else p1
            print(f'{p1}', end=',')
        if opcode == 5:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'If {p1} is not zero, then goto {p2}')
            if p1 != 0:
                ind = p2
                inc = 0
        if opcode == 6:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'If {p1} is zero, then goto {p2}')
            if p1 == 0:
                ind = p2
                inc = 0
        if opcode == 7:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'If {p1} < {p2}, setting position {p3} to 1')
            if p1 < p2:
                codes[p3] = 1
            else:
                codes[p3] = 0
        if opcode == 8:
            p1 = codes[p1] if m1 == 0 else p1
            p2 = codes[p2] if m2 == 0 else p2
            print(f'If {p1} = {p2}, setting position {p3} to 1')
            if p1 == p2:
                codes[p3] = 1
            else:
                codes[p3] = 0

        ind += inc
        opcode, m1, m2, m3 = get_mode(codes[ind])
    # print(codes)


print(f'Question 1')
# intcode_computer(inp=1, codes=codes)
print(f'Question 2')
intcode_computer(inp=5, codes=codes)
# intcode_computer(inp=7, codes=[3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#                                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#                                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
