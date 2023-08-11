from .test_core import TestCore

def list_equal(a, b):
    """
    Checks if cyclic lists a and b are equal.

    List contains points on a closed path, so you can choose any starting point,
    so it's not enough to check the equality of lists.
    """
    try:
        i = b.index(a[0])
    except ValueError:
        return False
    b = b[i:] + b[:i]
    return a == b

class Test(TestCore):
    def runtest(self, func):
        TestCore.test(self, 2, 1, self.test_func, func)

    def read_data(self, test_no):
        with open(f"../bitalg/tests/test2_tests/task1/test_2_1_{test_no}.in") as f:
            all_points = [(float(line.split()[0]), float(line.split()[1])) for line in f.readlines()]
        with open(f"../bitalg/tests/test2_tests/task1/test_2_1_{test_no}.out") as f:
            hull_points = [(float(line.split()[0]), float(line.split()[1])) for line in f.readlines()]
        return all_points, hull_points

    def test_func(self, test_no, func):
        test_input, test_answer = self.read_data(test_no)
        test_output = func(test_input)
        if list_equal(test_answer, test_output):
            return 1, None
        else:
            str_out = str(test_output) if len(str(test_output)) < 350 else str(test_output)[:350] + '...'
            str_ans = str(test_answer) if len(str(test_answer)) < 350 else str(test_answer)[:350] + '...'
            return 0, str_out, str_ans
