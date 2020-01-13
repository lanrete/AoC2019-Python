from intcode_computer import IntcodeComputer


class TestIntcodeComputer:
    def test_position_check_zero(self):
        com = IntcodeComputer(name='Position Check Zero',
                              codes=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])
        com.add_inputs([0])
        com.run()
        assert com.result == [0]

    def test_immediate_check_zero(self):
        com = IntcodeComputer(name='Immediate Check Zero',
                              codes=[3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
        com.add_inputs([0])
        com.run()
        assert com.result == [0]

    def test_compare_with_eight(self):
        com = IntcodeComputer(name='Compare with 8',
                              codes=[3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                     1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                     999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
        com.add_inputs([7, 8, 9])
        while com.inputs:
            com.run()
            com.reset()
        assert com.result == [999, 1000, 1001]

    def test_relative_mode(self):
        codes = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        com = IntcodeComputer(name='New Relative Mode',
                              codes=codes)
        com.run()
        assert com.result == codes

    def test_large_number(self):
        com = IntcodeComputer(name='Larger Number',
                              codes=[104, 12351231251321321, 99])
        com.run()
        assert com.result == [12351231251321321]

    def test_large_result(self):
        com = IntcodeComputer(name='Large Computation',
                              codes=[1102, 34915192, 34915192, 7, 4, 7, 99, 0])
        com.run()
        assert len(str(com.result[0])) == 16
