from itertools import permutations

DATA_DIR = '../input'

with open(f'{DATA_DIR}/7', 'r') as f:
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
    # print(s)


def intcode_computer_basic(inps: list, codes, start=0):
    ans = 0
    ind = 0
    code = codes[start:]
    inc_dict = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}
    opcode, m1, m2, m3 = get_mode(code[ind])
    while opcode != 99:
        p1 = get(code, ind + 1)
        p2 = get(code, ind + 2)
        p3 = get(code, ind + 3)
        get_status(opcode, p1, p2, p3)

        inc = inc_dict.get(opcode, 0)
        if opcode == 1:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'Adding {p1} and {p2} and putting the result into {p3}')
            code[p3] = p1 + p2
        if opcode == 2:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'Multiplying {p1} and {p2} and putting the result into {p3}')
            code[p3] = p1 * p2
        if opcode == 3:
            if inps:
                inp = inps.pop(0)
                print(f'Putting {inp} into position {p1}')
                code[p1] = inp
        if opcode == 4:
            p1 = code[p1] if m1 == 0 else p1
            ans = p1
            print(f'Outputting {p1}')
        if opcode == 5:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'If {p1} is not zero, then goto {p2}')
            if p1 != 0:
                ind = p2
                inc = 0
        if opcode == 6:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'If {p1} is zero, then goto {p2}')
            if p1 == 0:
                ind = p2
                inc = 0
        if opcode == 7:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'If {p1} < {p2}, setting position {p3} to 1')
            if p1 < p2:
                code[p3] = 1
            else:
                code[p3] = 0
        if opcode == 8:
            p1 = code[p1] if m1 == 0 else p1
            p2 = code[p2] if m2 == 0 else p2
            print(f'If {p1} = {p2}, setting position {p3} to 1')
            if p1 == p2:
                code[p3] = 1
            else:
                code[p3] = 0

        ind += inc
        opcode, m1, m2, m3 = get_mode(code[ind])
    return ans, 0
    # print(code)


def get_output_q1(phase, codes):
    out = 0
    for p in phase:
        inps = [p, out]
        out, _ = intcode_computer_basic(inps, codes)
    print(out)
    return out


res = []
for c in permutations(range(5), 5):
    res.append(get_output_q1(c, codes))
print(f'Question 1: {max(res)}')


