DATA_DIR = '../input'


def check_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1 == x2) & (x3 == x4):
        return False

    if (y1 == y2) & (y3 == y4):
        return False

    if (x1 == x2) & (y3 == y4):
        if ((x3 - x1) * (x4 - x1) < 0) & ((y1 - y3) * (y2 - y3) < 0):
            print(f'Cross at ({x1}, {y3})')
            return (x1, y3)
        return False

    if (y1 == y2) & (x3 == x4):
        if ((y3 - y1) * (y4 - y1) < 0) & ((x1 - x3) * (x2 - x3) < 0):
            print(f'Cross at ({x3}, {y1})')
            return (x3, y1)
        return False

    return False


def get_route(_):
    p = (0, 0)
    route = [p]
    for step in _.split(','):
        dir = step[0]
        l = int(step[1:])
        x, y = p
        if dir == 'U':
            p = (x, y + l)
        if dir == 'D':
            p = (x, y - l)
        if dir == 'L':
            p = (x - l, y)
        if dir == 'R':
            p = (x + l, y)
        route.append(p)
    return route


if __name__ == '__main__':
    with open(f'{DATA_DIR}/3', 'r') as f:
        _ = f.readline()
        r1 = get_route(_)
        _ = f.readline()
        r2 = get_route(_)

    print(f'{r1}\n{r2}')

    min_dis = 99999999999999
    for start1, end1 in zip(r1[:-1], r1[1:]):
        for start2, end2 in zip(r2[:-1], r2[1:]):
            x1, y1 = start1
            x2, y2 = end1

            x3, y3 = start2
            x4, y4 = end2

            cross = check_cross(x1, y1, x2, y2, x3, y3, x4, y4)
            if cross:
                dis = abs(cross[0]) + abs(cross[1])
                if (dis > 0) & (dis < min_dis):
                    min_dis = dis

    print(f'Question 1 : {min_dis}')
