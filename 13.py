from intcode_computer import IntcodeComputer

DATA_DIR = '../input'

with open(f'{DATA_DIR}/13', 'r') as f:
    r = f.readline()
    codes = [int(_) for _ in r.split(',')]
    computer = IntcodeComputer(name='Arcade Game', codes=codes)


def paint_result(intcode: IntcodeComputer, floor: dict):
    commands = intcode.result
    cnt = len(commands) // 3
    print(f'{cnt} result found')

    for _ in range(cnt):
        x = commands[_ * 3]
        y = commands[_ * 3 + 1]
        tile_id = commands[_ * 3 + 2]
        floor[(x, y)] = tile_id

    k = floor.keys()
    max_x = max([_[0] for _ in k])
    max_y = max([_[1] for _ in k])

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            tile = floor.get((x, y), 0)
            if tile == 0:
                print(' ', end='')
            if tile == 1:
                print('#', end='')
            if tile == 2:
                print('$', end='')
            if tile == 3:
                print('=', end='')
            if tile == 4:
                print('O', end='')
        print('')
    print(f'Score: {floor.get((-1, 0), "Missing")}')
    intcode.result = []


free_play = codes.copy()
free_play[0] = 2
arcade = IntcodeComputer('Arcade', free_play)

arcade.run()
floor = {}
paint_result(arcade, floor)
while arcade.pending_input:
    joystick_input = input('-1, 0 or 1?')
    while joystick_input not in ['-1', '0', '1']:
        joystick_input = input('-1, 0 or 1?')
    joystick_input = int(joystick_input)
    arcade.add_inputs([joystick_input])
    arcade.run()
    paint_result(arcade, floor)
