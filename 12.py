DATA_DIR = '../input'


class Moon:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.pot = self.x + self.y + self.z
        self.kin = 0
        self.energy = 0

    def get_mark(self):
        return f'{self.x}{self.y}{self.z}{self.vx}{self.vy}{self.vz}'

    def get_pot(self):
        self.pot = abs(self.x) + abs(self.y) + abs(self.z)
        return self.pot

    def get_kin(self):
        self.kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return self.kin

    def get_energy(self):
        p = self.get_pot()
        k = self.get_kin()
        self.energy = p * k
        return self.energy

    def apply_gravity(self, other_moons):
        for moon in other_moons:
            if self.x < moon.x:
                self.vx += 1
            if self.x > moon.x:
                self.vx -= 1
            if self.y < moon.y:
                self.vy += 1
            if self.y > moon.y:
                self.vy -= 1
            if self.z < moon.z:
                self.vz += 1
            if self.z > moon.z:
                self.vz -= 1

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        # print(f'{self.name:10} is at ({self.x:3}, {self.y:3}, {self.z:3}), '
        #       f'with velocity: ({self.vx:2}, {self.vy:2}, {self.vz:2})')


def get_input():
    moons = []
    with open(f'{DATA_DIR}/12', 'r') as f:
        names = ['Io', 'Europa', 'Ganymede', 'Callisto']
        stats = f.readlines()
        for stat, name in zip(stats, names):
            _ = stat.strip().split(',')
            x = int(_[0][3:])
            y = int(_[1][3:])
            z = int(_[2][3:-1])
            moon = Moon(name, x, y, z)
            moons.append(moon)
    return moons


jupyter_moons = get_input()

for iteration in range(1000):
    # print(f'Iteration: {iteration + 1}')
    for each_moon in jupyter_moons:
        others = jupyter_moons.copy()
        others.remove(each_moon)
        each_moon.apply_gravity(others)
    for each_moon in jupyter_moons:
        each_moon.apply_velocity()
    # print('')
print(f'Total energy: {sum([_.get_energy() for _ in jupyter_moons])}')

jupyter_moons = get_input()
step = 0
seen = set()
while True:
    step += 1
    for each_moon in jupyter_moons:
        others = jupyter_moons.copy()
        others.remove(each_moon)
        each_moon.apply_gravity(others)
    for each_moon in jupyter_moons:
        each_moon.apply_velocity()
    marks = [_.get_mark() for _ in jupyter_moons]
    marks = ''.join(marks)
    if marks in seen:
        print(f'Same after {step} steps')
        break
    else:
        seen.add(marks)
        print(f'{step:10}: {marks}')
# TODO How to simulate this more efficiently
