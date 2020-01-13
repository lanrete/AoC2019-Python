from utl import block

DATA_DIR = '../input'


def print_image(_):
    show_dict = {1: '1', 0: '0', 2: ' '}
    shown = [show_dict[p] for p in _]
    print(''.join(shown))


with open(f'{DATA_DIR}/8', 'r') as f:
    inp = f.readline().strip()
    inp = [int(_) for _ in inp]
    width = 25
    height = 6
    size = width * height

    chunk = int(len(inp) / size)

m = size
ans = m
final_image = [2] * size
mod_cnt = 0
for layer in range(chunk):
    layer_pixel = inp[size * layer:size * (layer + 1)]
    with block('Question 1'):
        current_zero_cnt = sum([1 if _ == 0 else 0 for _ in layer_pixel])
        current_one_cnt = sum([1 if _ == 1 else 0 for _ in layer_pixel])
        current_two_cnt = sum([1 if _ == 2 else 0 for _ in layer_pixel])

        if current_zero_cnt < m:
            m = current_zero_cnt
            ans = current_one_cnt * current_two_cnt

    with block('Question 2'):
        for ind, pixel in enumerate(layer_pixel, 0):
            if pixel == 2:
                continue
            if final_image[ind] != 2:
                continue
            final_image[ind] = pixel
            mod_cnt += 1
        print(f'-' * size)
        print(f'Layer {layer}')
        print_image(layer_pixel)
        print(f'After layer {layer}, {mod_cnt} pixels are changed')
        print_image(final_image)

print(f'-' * size)
print(f'Question 1: {ans}')

for ind, c in enumerate(final_image, 1):
    if c == 0:
        c = ' '
    if ind % width != 0:
        print(c, end='')
    if ind % width == 0:
        print(c)

final_image = [2] * size
for layer in reversed(range(chunk)):
    layer_pixel = inp[size * layer:size * (layer + 1)]

    with block('Question 2'):
        for ind, pixel in enumerate(layer_pixel, 0):
            if pixel == 2:
                continue
            final_image[ind] = pixel
print_image(final_image)

