from .test_core import TestCore
from numpy import linalg, array
from random import uniform

class Test(TestCore):
    def runtest(self, task_no, *func):
        """
            Checks the correctness of the function
            :param task_no: number of task
            :param func: name of functions to test
            :return:
        """
        if task_no == 1:
            TestCore.test(self, 1, 1, self.task1_func, *func)
        else:
            TestCore.test(self, 1, 2, self.task2_func, *func)

    # 10**5 numbers from interval [-1000, 1000]
    # 10**5 numbers from interval [-10**14, 10**14]
    # 1000 on circle (S=(0,0), r=100)
    # 1000 z [-1000, 1000] on line created by vector ([-1, 0], [1, 0.1])
    @staticmethod
    def task1_func(test_no, *func):
        EPS = 10 ** -10
        if test_no == 1:
            Result = func[0](-1000, 1000)
            if len(Result) != 10 ** 5:
                return 0, "[len: {}]".format(len(Result)), "[len: 10^5]"
            for x, y in Result:
                if x < -1000 or x > 1000 or y < -1000 or y > 1000:
                    return 0, "[{}, {}]".format(x, y), "[-1000, 1000]"
            return 1, None

        elif test_no == 2:
            low, high = -10 ** 14, 10 ** 14
            Result = func[0](low, high)
            if len(Result) != 10 ** 5:
                return 0, "[len: {}]".format(len(Result)), "[len: 10^5]"
            for x, y in Result:
                if x < low or x > high or y < low or y > high:
                    return 0, "[{}, {}]".format(x, y), "[-10**14, 10**14]"
            return 1, None

        elif test_no == 3:
            Result = func[1]((0, 0), 100, 1000)
            if len(Result) != 1000:
                return 0, "[len: {}]".format(len(Result)), "[len: 1000]"
            for x, y in Result:
                if abs((x ** 2 + y ** 2) - 10000) > EPS:
                    print((x ** 2 + y ** 2))
                    return 0, "[{}, {}]".format(x, y), "[Not on circle]"
            return 1, None

        else:
            Result = func[2]((-1.0, 0.0), (1.0,0.1), 1000)
            if len(Result) != 1000:
                return 0, "[len: {}]".format(len(Result)), "[len: 1000]"
            for x, y in Result:
                if abs(0.05 * x + 0.05 - y) > EPS:
                    return 0, "[{}, {}]".format(x, y), "[Not on line]"
            return 1, None

    # matrix determinant
    @staticmethod
    def task2_func(test_no, *func):
        EPS = 10 ** -10
        if test_no == 1:
            Input = [[[uniform(-100, 100), uniform(-100, 100)] for _ in range(3)] for _ in range(10)]
            for a, b, c in Input:
                Result = func[0](a, b, c)
                if abs(Result - linalg.det(array([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]]))) > EPS:
                    return 0, "{}".format(Result), "{}".format(
                        linalg.det(array([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]])))
            return 1, None

        else:
            Input = [[[uniform(-100, 100), uniform(-100, 100)] for _ in range(3)] for _ in range(10)]
            for a, b, c in Input:
                Result = func[1](a, b, c)
                if abs(Result - linalg.det(array([[a[0] - c[0], a[1] - c[1]], [b[0] - c[0], b[1] - c[1]]]))) > EPS:
                    return 0, "{}".format(Result), "{}".format(
                        linalg.det(array([[a[0] - c[0], a[1] - c[1]], [b[0] - c[0], b[1] - c[1]]])))
            return 1, None
