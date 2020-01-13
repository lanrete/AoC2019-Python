from math import gcd

DATA_DIR = '../input'

with open(f'{DATA_DIR}/10', 'r') as f:
    maps = f.readlines()
    maps = [_.strip() for _ in maps]
    mapping = {
        '#': 1,
        '.': 0
    }
    maps = [[mapping[_] for _ in __] for __ in maps]
    h = len(maps)
    w = len(maps[0])
    print(f'Height: {h}')
    print(f'Width: {w}')


def next_upper_left(x, y):
    if x > 0:
        return x - 1, y
    if y > 0:
        return w - 1, y - 1
    return None, None


def next_lower_right(x, y):
    if x < w - 1:
        return x + 1, y
    if y < h - 1:
        return 0, y + 1
    return None, None


def valid(x, y):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= w:
        return False
    if y >= h:
        return False
    return True


def extend_star(x, y, tx, ty):
    gap_x = tx - x
    gap_y = ty - y

    g = gcd(gap_x, gap_y)
    gap_x = int(gap_x / g)
    gap_y = int(gap_y / g)

    new_x = tx + gap_x
    new_y = ty + gap_y
    while valid(new_x, new_y):
        yield new_x, new_y
        new_x = new_x + gap_x
        new_y = new_y + gap_y


def iterate_stars(x, y):
    nx, ny = x, y
    while (nx is not None) and ((nx != 0) or (ny != 0)):
        nx, ny = next_upper_left(nx, ny)
        yield nx, ny
    nx, ny = x, y
    while (nx is not None) and ((nx != w - 1) or (ny != h - 1)):
        nx, ny = next_lower_right(nx, ny)
        yield nx, ny


def check_visibility(x, y):
    vis = [[-1 for _ in range(w)] for _ in range(h)]
    vis[y][x] = False
    star_list = []
    for nx, ny in iterate_stars(x, y):
        if maps[ny][nx] == 1:
            """
            If there is a star at (nx, ny) & (nx, ny) is visible 
            Add (nx, ny) to the seen list
            Modify every location on the extended line from (x, y) to (nx, ny) as invisible
            """
            if vis[ny][nx] == -1:
                vis[ny][nx] = True
                star_list.append((nx, ny))
                for sx, sy in extend_star(x, y, nx, ny):
                    vis[sy][sx] = False

    ans = len(star_list)
    print(f'{ans} stars can be seen at ({x}, {y})')
    return len(star_list), ans


ans = 0
ans_x, ans_y = None, None
for x in range(w):
    for y in range(h):
        t = check_visibility(x, y)
        if t > ans:
            ans, _ = t
            ans_x = x
            ans_y = y
print(f'Q1: {ans} at ({ans_x}, {ans_y})')


ox = 19
oy = 14
destroy_cnt = 0
while True:
    cnt, stars = check_visibility(ox, oy)
    if cnt == 0:
        print('All stars destroyed')
        break
