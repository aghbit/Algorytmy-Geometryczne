from .test_core import TestCore

class Test(TestCore):
    def runtest(self, func):
        TestCore.test(self, 2, 1, self.test_func, func)

    def read_data(self, test_no):
        # TODO change path
        with open(f"bitalg/tests/test2_tests/task1/test_2_1_{test_no}.in") as f:
            all_points = [(float(line.split()[0]), float(line.split()[1])) for line in f.readlines()]
        with open(f"bitalg/tests/test2_tests/task1/test_2_1_{test_no}.out") as f:
            hull_points = [(float(line.split()[0]), float(line.split()[1])) for line in f.readlines()]
        return all_points, hull_points

    def test_func(self, test_no, func):
        test_input, test_answer = self.read_data(test_no)
        test_output = func(test_input)
        if test_output == test_answer:
            return 1, None
        else:
            return 0, test_output, test_answer