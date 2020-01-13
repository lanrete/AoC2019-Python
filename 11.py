from intcode_computer import IntcodeComputer

DATA_DIR = '../input'

with open(f'{DATA_DIR}/11', 'r') as f:
    r = f.readline()
    codes = [int(_) for _ in r.split(',')]


def turn(pre_dir, turn_dir):
    if turn_dir == 0:
        return (pre_dir + 4 - 1) % 4
    if turn_dir == 1:
        return (pre_dir + 1) % 4


def forward(loc, direction):
    x, y = loc
    if direction == 0:
        return x, y + 1
    if direction == 1:
        return x + 1, y
    if direction == 2:
        return x, y - 1
    if direction == 3:
        return x - 1, y


def get_color(floor, location):
    return floor.get(location, 0)


def paint(start_color):
    computer = IntcodeComputer(name='painting robot', codes=codes)
    floor = dict()
    robot_location = (0, 0)
    floor[robot_location] = start_color
    robot_state = 1
    # Direction:
    # 0 -> Up
    # 1 -> Right
    # 2 -> Down
    # 3 -> Left
    robot_direction = 0

    while not computer.complete:
        current_color = get_color(floor, robot_location)
        computer.add_inputs([current_color])
        computer.run()
        while computer.result:
            result = computer.result.pop(0)
            # robot state 1  -> Paint the floor
            if robot_state == 1:
                floor[robot_location] = result
            # robot state -1 -> Turns
            else:
                robot_direction = turn(robot_direction, result)
                robot_location = forward(robot_location, robot_direction)
            robot_state *= -1
    return floor


black_start_floor = paint(0)
print(f'{len(black_start_floor)} panels have been painted')


def paint_floor(floor: dict, c):
    keys = floor.keys()
    min_x = min([_[0] for _ in keys])
    max_x = max([_[0] for _ in keys])
    min_y = min([_[1] for _ in keys])
    max_y = max([_[1] for _ in keys])

    for y in range(max_y + 1, min_y - 1, -1):
        for x in range(min_x - 1, max_x + 1):
            if get_color(floor, (x, y)) == 1:
                print(c, end='')
            else:
                print(' ', end='')
        print('')


white_start_floor = paint(1)
paint_floor(white_start_floor, '#')
