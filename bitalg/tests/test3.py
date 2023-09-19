from .test_core import TestCore, get_test_path

class Test(TestCore):
    def runtest(self, task_no, func):
        """
        Checks the correctness of the function
        :param task_no: number of task
        :param func: name of function to test
        :return:
        """
        if task_no == 1:
            TestCore.test(self, 3, 1, self.task1_func, func)
        elif task_no == 2:
            TestCore.test(self, 3, 2, self.task2_func, func)
        else:
            TestCore.test(self, 3, 3, self.task3_func, func)

    @staticmethod
    def read_data(task_no, test_no):
        try:
            with open(get_test_path(3, task_no, test_no) + ".in") as f:
                Points = [(float(line.split()[0]), float(line.split()[1])) for line in f.readlines()]
                return Points
        except FileNotFoundError:
            print(f"ERROR: File not found ({get_test_path(3, task_no, test_no)}.in)")
            return []

    # is y-monotone
    def task1_func(self, test_no, func):
        Input = self.read_data(1, test_no)
        try:
            Output = open(get_test_path(3, 1, test_no) + ".out").read()
        except FileNotFoundError:
            print(f"ERROR: File not found ({get_test_path(3, 1, test_no)}.out)")
            return 0, None, None
        Result = func(Input)
        if str(Result) == Output:
            return 1, None
        return 0, Result, Output

    # vertex classification (początkowe, końcowe, łączące, dzielące i prawidłowe)
    def task2_func(self, test_no, func):
        Input = self.read_data(2, test_no)
        try:
            Output = list(map(int, open(get_test_path(3, 2, test_no) + ".out").read().split("\n")))
        except FileNotFoundError:
            print(f"ERROR: File not found ({get_test_path(3, 1, test_no)}.out)")
            return 0, None, None
        Result = func(Input)
        if Result == Output:
            return 1, None
        return 0, Result, Output

    # triangulation with steps
    def task3_func(self, test_no, func):
        Input = self.read_data(3, test_no)
        try:
            Output = [[int(i) for i in line.strip().split(' ')] for line in open(get_test_path(3, 3, test_no) + ".out").readlines()]
        except FileNotFoundError:
            print(f"ERROR: File not found ({get_test_path(3, 3, test_no)}.out)")
            return 0, None, None
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
