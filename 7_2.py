from itertools import permutations

from intcode_computer import IntcodeComputer

DATA_DIR = '../input'

with open(f'{DATA_DIR}/7', 'r') as f:
    raw = f.readline()
    codes = [int(_) for _ in raw.split(',')]


def find_biggest_output(phases, codes):
    amps = [IntcodeComputer(f'Amp {i}', codes) for i in range(5)]
    for amp, phase in zip(amps, phases):
        amp.add_inputs([phase])
    amps[0].add_inputs([0])

    keep_running = [True for _ in range(5)]
    candidates = []
    i = 0
    while any(keep_running):
        i += 1
        for ind, amp in enumerate(amps):
            print(f'Running {amp.name}')
            print(f'Inputs of {amp.name}: {amp.inputs}')
            amp.run()
            output = amp.result
            j = (ind + 1) % 5
            amps[j].add_inputs(output)
            if j == 0:
                candidates.extend(output)
            print(f'Adding {output} to {amps[j].name}')
            amp.result = []
            if amp.pending_input is False:
                keep_running[ind] = False
        print(f'Iteration {i}')
    return max(candidates)


m = 0
for phase in permutations(range(5, 10), 5):
    m = max(m, find_biggest_output(phase, codes))
print(m)
