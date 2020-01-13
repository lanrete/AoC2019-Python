from intcode_computer import IntcodeComputer
DATA_DIR = '../input'

with open(f'{DATA_DIR}/9', 'r') as f:
    r = f.readline()
    codes = [int(_) for _ in r.split(',')]

com = IntcodeComputer(
    name='Complete Computer',
    codes=codes,
    # verbose=1,
)
# com.add_inputs([1])
# com.run()
# print(f'Question 1: {com.result}')

com.reset()
com.add_inputs([2])
com.run()
print(f'Question 2: {com.result}')

