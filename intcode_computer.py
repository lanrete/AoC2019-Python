class IntcodeComputer:
    def __init__(self, name: str, codes: list, verbose=0):
        self.name = name
        self.pointer = 0
        self.codes = codes.copy()
        self.codes = {
            ind: v for ind, v in enumerate(codes)
        }
        self.inputs = []
        self.op_dict = {
            1: self.op1,
            2: self.op2,
            3: self.op3,
            4: self.op4,
            5: self.op5,
            6: self.op6,
            7: self.op7,
            8: self.op8,
            9: self.op9,
        }
        self.result = []
        self.pending_input = False
        self.complete = False
        self.verbose = verbose
        self.relative_base = 0
        return

    def parse_mode(self):
        instruction = self.codes[self.pointer]
        opcode = instruction % 100
        m1 = (instruction % 1000) // 100
        m2 = (instruction % 10000) // 1000
        m3 = instruction // 10000
        return opcode, m1, m2, m3

    def add_inputs(self, inputs: list):
        self.inputs.extend(inputs)
        self.pending_input = False

    def reset(self):
        self.pointer = 0

    def run(self):
        opcode, m1, m2, m3 = self.parse_mode()
        while opcode != 99:
            p1 = self.get_pos(self.pointer + 1)
            p2 = self.get_pos(self.pointer + 2)
            p3 = self.get_pos(self.pointer + 3)
            func = self.op_dict[opcode]
            res = func.__call__(p1=p1, p2=p2, p3=p3, m1=m1, m2=m2, m3=m3)
            if res is False:
                print(f'{self.name} need more input')
                self.pending_input = True
                break
            if res is not None:
                self.result.append(res)
            opcode, m1, m2, m3 = self.parse_mode()
        if opcode == 99:
            self.complete = True
        return

    def get_pos(self, position):
        return self.codes.get(position, 0)

    def get_value(self, parameter, mode):
        if mode == 0:
            return self.codes.get(parameter, 0)
        if mode == 1:
            return parameter
        if mode == 2:
            return self.codes.get(self.relative_base + parameter, 0)

    def op1(self, p1, p2, p3, m1, m2, m3, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        v3 = p3 if m3 == 0 else self.relative_base + p3
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 4)]))
            print(f'Adding {v1} and {v2} and putting the result into {v3}')
        self.codes[v3] = v1 + v2
        self.pointer += 4
        return

    def op2(self, p1, p2, p3, m1, m2, m3, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        v3 = p3 if m3 == 0 else self.relative_base + p3
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 4)]))
            print(f'Multiplying {v1} and {v2} and putting the result into {v3}')
        self.codes[v3] = v1 * v2
        self.pointer += 4
        return

    def op3(self, p1, m1, **kwargs):
        v1 = p1 if m1 == 0 else self.relative_base + p1
        if self.inputs:
            inp = self.inputs.pop(0)
            if self.verbose > 0:
                print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 2)]))
                print(f'Putting {inp} into {v1}')
            self.codes[v1] = inp
            self.pointer += 2
            return
        if self.verbose > 0:
            print('Need more input')
        return False

    def op4(self, p1, m1, **kwargs):
        v1 = self.get_value(p1, m1)
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 2)]))
            print(f'Outputting {v1}')
        self.pointer += 2
        return v1

    def op5(self, p1, p2, m1, m2, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 3)]))
            print(f'If {v1} is not zero, then goto {v2}')
        if v1 != 0:
            self.pointer = v2
        else:
            self.pointer += 3
        return

    def op6(self, p1, p2, m1, m2, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 3)]))
            print(f'If {v1} is zero, then goto {v2}')
        if v1 == 0:
            self.pointer = v2
        else:
            self.pointer += 3
        return

    def op7(self, p1, p2, p3, m1, m2, m3, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        v3 = p3 if m3 == 0 else self.relative_base + p3
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 4)]))
            print(f'If {v1} < {v2}, setting position {v3} to 1, else 0')
        if v1 < v2:
            self.codes[v3] = 1
        else:
            self.codes[v3] = 0
        self.pointer += 4
        return

    def op8(self, p1, p2, p3, m1, m2, m3, **kwargs):
        v1 = self.get_value(p1, m1)
        v2 = self.get_value(p2, m2)
        v3 = p3 if m3 == 0 else self.relative_base + p3
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 4)]))
            print(f'If {v1} = {v2}, setting position {v3} to 1, else 0')
        if v1 == v2:
            self.codes[v3] = 1
        else:
            self.codes[v3] = 0
        self.pointer += 4
        return

    def op9(self, p1, m1, **kwargs):
        v1 = self.get_value(p1, m1)
        self.relative_base += v1
        if self.verbose > 0:
            print(','.join([str(self.codes.get(_, 0)) for _ in range(self.pointer, self.pointer + 2)]))
            print(f'Changing the relative base by adding {v1}')
            print(f'Relative base is now {self.relative_base}')
        self.pointer += 2
