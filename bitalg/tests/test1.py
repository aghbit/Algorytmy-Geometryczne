from test_core import TestCore
from numpy import linalg
from random import uniform
import numpy


class Test(TestCore):
    def runtest(self, task_no, EPS, *func):
        if task_no == 1:
            TestCore.test(self, 1, 1, self.task1_func, EPS, *func)
        else:
            TestCore.test(self, 1, 2, self.task2_func, EPS, *func)

    # 10**5 z zakresu [-1000, 1000]
    # 10**5 z zakresu [-10**14, 10**14]
    # 1000 z okręgu (S=(0,0), r=100)
    # 1000 z [-1000, 1000] na prostej wektora ([-1, 0], [1, 0.1])
    def task1_func(self, test_no, EPS, *func):
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
            Result = func[1]()
            if len(Result) != 1000:
                return 0, "[len: {}]".format(len(Result)), "[len: 1000]"
            for x, y in Result:
                if abs((x ** 2 + y ** 2) - 10000) > EPS:
                    print((x ** 2 + y ** 2))
                    return 0, "[{}, {}]".format(x, y), "[Not on circle]"
            return 1, None

        else:
            Result = func[2]()
            if len(Result) != 1000:
                return 0, "[len: {}]".format(len(Result)), "[len: 1000]"
            for x, y in Result:
                if abs(0.05 * x + 0.05 - y) > EPS:
                    return 0, "[{}, {}]".format(x, y), "[Not on line]"
            return 1, None

    # matrix determinant
    def task2_func(self, test_no, EPS, *func):
        if test_no == 1:
            Input = [[[uniform(-100, 100), uniform(-100, 100)] for _ in range(3)] for _ in range(10)]
            for a, b, c in Input:
                Result = func[0](a, b, c)
                if abs(Result - linalg.det(numpy.array([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]]))) > EPS:
                    return 0, "{}".format(Result), "{}".format(
                        linalg.det(numpy.array([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]])))
            return 1, None

        else:
            Input = [[[uniform(-100, 100), uniform(-100, 100)] for _ in range(3)] for _ in range(10)]
            for a, b, c in Input:
                Result = func[1](a, b, c)
                if abs(Result - linalg.det(
                        numpy.array([[a[0] - c[0], a[1] - c[1]], [b[0] - c[0], b[1] - c[1]]]))) > EPS:
                    return 0, "{}".format(Result), "{}".format(
                        linalg.det(numpy.array([[a[0] - c[0], a[1] - c[1]], [b[0] - c[0], b[1] - c[1]]])))
            return 1, None

"""
# test ------------------------------------------------------------------------------------------------
def a(r, t):
    return numpy.random.uniform(r, t, size=[10 ** 5, 2])


def c():
    data_c = [None for _ in range(1000)]
    for i in range(1000):
        alpha = 2 * numpy.pi * numpy.random.random_sample()
        data_c[i] = (100 * numpy.cos(alpha), 100 * numpy.sin(alpha))
    return data_c


def d():
    data_d = [None for _ in range(1000)]
    for i in range(1000):
        x = numpy.random.uniform(-1000, 1000)
        data_d[i] = (x, 0.05 * x + 0.05)
    return data_d


def m3(a, b, c):
    return linalg.det(numpy.array([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]]))


def m2(a, b, c):
    return linalg.det(numpy.array([[a[0] - c[0], a[1] - c[1]], [b[0] - c[0], b[1] - c[1]]]))


x = Test()
x.runtest(1, 10 ** -10, a, c, d)
x.runtest(2, 10 ** -14, m3, m2)
"""