DATA_DIR = '../input'

with open(f'{DATA_DIR}/2', 'r') as f:
    ops = f.readline()
    ori_code = [int(_) for _ in ops.split(',')]


def intcode_computer(noun, verb):
    code = ori_code.copy()
    code[1] = noun
    code[2] = verb
    count = len(code) // 4

    for i in range(count):
        base = i * 4
        ops = code[base]
        if ops == 99:
            return code[0]
        a = code[base + 1]
        b = code[base + 2]
        c = code[base + 3]

        if ops == 1:
            code[c] = code[a] + code[b]
        if ops == 2:
            code[c] = code[a] * code[b]
    raise Exception('No 99')


print(f'Question 1: {intcode_computer(12, 2)}')

for n in range(100):
    for v in range(100):
        if intcode_computer(n, v) == 19690720:
            print(f'Question 2: {100 * n + v}')
            break

if __name__ == '__main__':
    pass
