from bitalg.tests.test_core import TestCore

class Test(TestCore):
    def __init__(self):
        super().__init__()
    def runtest(self, task_no, func):
        if task_no == 1:
            TestCore.test(self, 4, 1, self.task1_func, func)


    def read_data(self, task_no, test_no):
        Points = []
        # TODO ścieżki do zmiany
        for point in open("../tests/test4_tests/task{}/test_{}_{}_{}.in".format(task_no, 4, task_no, test_no), "r"):
            Points.append(list(map(float, point.split(" "))))
        return Points

    # test of orient function (orientation of three points given)
    def task1_func(self, test_no, func):
        Input = self.read_data(1, test_no)
        Output = open("../tests/test4_tests/task1/test_4_1_{}.out".format(test_no), "r").read()
        Result = func(Input[0], Input[1], Input[2])
        if str(Result) == Output:
            return 1, None
        return 0, Result, Output

