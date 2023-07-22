from test_core import TestCore

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
        for point in open("test3_tests\\task{}\\test_{}_{}_{}.in".format(task_no, 3, task_no, test_no), "rt"):
            Points.append(list(map(float, point.split(" "))))
        return Points

    # is y-monotone
    def task1_func(self, test_no, func):
        Input = self.read_data(1, test_no)
        Output = open("test3_tests\\task1\\test_3_1_{}.out".format(test_no), "r").read()
        Result = func(Input)
        if str(Result) == Output:
            return 1, Result, Output
        return 0, Result, Output

    # vertex classification (początkowe, końcowe, łączące, dzielące i prawidłowe)
    def task2_func(self, test_no, func):
        Input = self.read_data(2, test_no)
        Output = list(map(int, open("test3_tests\\task2\\test_3_2_{}.out".format(test_no), "r").read().split("\n")))
        Result = func(Input)
        if Result == Output:
            return 1, Result, Output
        return 0, Result, Output

    # triangulation with steps
    def task3_func(self, test_no, func):
        Input = self.read_data(3, test_no)
        Output = 4#list(map(int, open("test3_tests\\task3\\test_3_3_{}.out".format(test_no), "r").read().split("\n")))
        Result = func(Input)
        if Result == Output:
            return 1, Result, Output
        return 0, Result, Output

# task 1 test --------------------------------------------------------------------------------------------------------
""" 
EPS = 1e-12
def orient(a, b, c):
    return a[0]*b[1] + a[1]*c[0] + b[0]*c[1] - b[1]*c[0] - a[1]*b[0] - a[0]*c[1]

def is_connective_or_separative(a, b, c):
    determinant = orient(a, b, c)
    if a[1] > b[1] and c[1] > b[1] and determinant < -EPS:
        return True
    elif a[1] < b[1] and c[1] < b[1] and determinant < -EPS:
        return True
    return False


def monoton(points):
    for i in range(0, len(points) - 1):
        if is_connective_or_separative(points[i - 1], points[i], points[i + 1]):
            return False

    if is_connective_or_separative(points[-2], points[-1], points[0]):
        return False
    return True

x = Test()
x.runtest(1, monoton)
"""
# task 2 test --------------------------------------------------------------------------------------------------------
"""
def orient(a, b, c):
    return a[0]*b[1] + a[1]*c[0] + b[0]*c[1] - b[1]*c[0] - a[1]*b[0] - a[0]*c[1]

def qualify_vertexes(p):
    n = len(p)

    result = [-1]*n

    for i in range(n):
        prev_point = p[(i - 1) % n]
        current_point = p[i]
        next_point = p[(i + 1) % n]

        o = orient(prev_point, current_point, next_point)
        above = 0

        if prev_point[1] > current_point[1]:
            above += 1
        if next_point[1] > current_point[1]:
            above += 1

        if above == 0:
            if o > 0:
                result[i] = 0 # beginning_points.append(current_point)
            else:
                result[i] = 3 # dividing_points.append(current_point)
        elif above == 2:
            if o > 0:
                result[i] = 1 # ending_points.append(current_point)
            else:
                result[i] = 2 # connecting_points.append(current_point)
        else:
            result[i] = 4 # correct_points.append(current_point)

    return result


x = Test()
x.runtest(2, qualify_vertexes)
"""
# task 3 test --------------------------------------------------------------------------------------------------------

...

# end_of_file ---------------------------------------------------------------------------------------------------------