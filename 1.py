DATA_DIR = '../input'

ans = 0
with open(f'{DATA_DIR}/1', 'r') as f:
    for _ in f.readlines():
        ans += (int(_) // 3 - 2)

print(f'Question 1: {ans}')

ans = 0
with open(f'{DATA_DIR}/1', 'r') as f:
    for _ in f.readlines():
        mass = int(_)
        while mass > 0:
            fuel = mass // 3 - 2
            if fuel > 0:
                ans += fuel
                mass = fuel
            else:
                mass = 0

print(f'Question 2: {ans}')

if __name__ == '__main__':
    pass