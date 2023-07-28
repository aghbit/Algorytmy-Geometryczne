from .test_core import TestCore

class Test(TestCore):
    def runtest(self, task_no, func):
        if task_no == 1:
            TestCore.test(self, 3, 1, self.task1_func, func)
        elif task_no == 2:
            TestCore.test(self, 3, 2, self.task2_func, func)
        else:
            TestCore.test(self, 3, 3, self.task3_func, func)

    def read_data(self, task_no, test_no):
        Points = []
        for point in open("..\\bitalg\\tests\\test3_tests\\task{}\\test_{}_{}_{}.in".format(task_no, 3, task_no, test_no), "r"):
            Points.append(list(map(float, point.split(" "))))
        return Points

    # is y-monotone
    def task1_func(self, test_no, func):
        Input = self.read_data(1, test_no)
        Output = open("..\\bitalg\\tests\\test3_tests\\task1\\test_3_1_{}.out".format(test_no), "r").read()
        Result = func(Input)
        if str(Result) == Output:
            return 1, None
        return 0, Result, Output

    # vertex classification (początkowe, końcowe, łączące, dzielące i prawidłowe)
    def task2_func(self, test_no, func):
        Input = self.read_data(2, test_no)
        Output = list(map(int, open("..\\bitalg\\tests\\test3_tests\\task2\\test_3_2_{}.out".format(test_no), "r").read().split("\n")))
        Result = func(Input)
        if Result == Output:
            return 1, None
        return 0, Result, Output

    # triangulation with steps
    def task3_func(self, test_no, func):
        Input = self.read_data(3, test_no)
        Output = [[int(i) for i in line.strip().split(' ')] for line in
                  open("..\\bitalg\\tests\\test3_tests\\task3\\test_3_3_{}.out".format(test_no), "r").readlines()]
        Result = func(Input)

        if len(Result) != len(Output):
            return 0, Result, Output

        Check_O = [False] * len(Output)
        Check_R = [False] * len(Result)

        for i in range(len(Output)):
            if Check_O[i]:
                continue
            for j in range(len(Output)):
                if Check_R[j]:
                    continue
                if (Output[i][0] == Result[j][0] and Output[i][1] == Result[j][1]) or \
                   (Output[i][0] == Result[j][1] and Output[i][1] == Result[j][0]):
                    Check_O[i] = True
                    Check_R[j] = True

        for i in range(len(Output)):
            if not Check_O[i]:
                return 0, Result, Output
        for i in range(len(Output)):
            if not Check_R[i]:
                return 0, Result, Output
        return 1, None
