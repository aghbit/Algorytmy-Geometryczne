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
        for point in open("test3_tests\\task{}\\test_{}_{}_{}.in".format(task_no, 3, task_no, test_no), "r"):
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
        Output = [[int(i) for i in line.strip().split(' ')] for line in
                  open("test3_tests\\task3\\test_3_3_{}.out".format(test_no), "r").readlines()]
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
        return 1, Result, Output

# julek
"""
# task 1 test --------------------------------------------------------------------------------------------------------

EPS = 1e-12
def orient(a, b, c):
    return a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - b[1] * c[0] - a[1] * b[0] - a[0] * c[1]


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

# task 2 test --------------------------------------------------------------------------------------------------------

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

x.runtest(2, qualify_vertexes)

# task 3 test --------------------------------------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chain = None
        self.index = None

    def set_chain(self, chain):
        self.chain = chain

    def get_coords(self):
        return self.x, self.y


def map_to_points_and_lines(p):
    n = len(p)
    L = [(p[i], p[(i + 1) % n]) for i in range(n)]
    P = [Point(p[i][0], p[i][1]) for i in range(n)]

    return P, L


def inside_polygon(a, b, c,
                   chain):  # funkcja sprawdzająca czy trójkąt złożony z punktów a,b,c leży całkowicie w wielokącie
    o = orient(a, b, c)

    if abs(o) < EPS:
        return False  # czy punkty są współniniowe

    if chain == 1:  # zależnie od łańcucha inaczej sprawdzam ten trójkąt
        return o < 0
    else:
        return o > 0


def do_not_follow(p1, p2,
                  n):  # czy punkty p1 i p2 nie są kolejnymi punktami w wieloącie (tzn czy międy p1 i p2 nie ma jeszcze krawędzi)
    return abs(p1.index - p2.index) != 1 and abs(p1.index - p2.index) != n - 1


def triangulate(p):
    if not monoton(p):  # czy wielokąt jest monotoniczny
        print('Wielokąt nie jest monotoniczny!')
        return None, None

    P, L = map_to_points_and_lines(p)  # zamiana na kasę Point
    n = len(P)

    min_index = P.index(min(P, key=lambda v: v.y))
    max_index = P.index(max(P, key=lambda v: v.y))

    x = max_index  # uzupełnienie pól klasy point
    while x != min_index:
        P[x].chain = 1
        P[x].index = x
        x = (x + 1) % n

    while x != max_index:
        P[x].chain = 2
        P[x].index = x
        x = (x + 1) % n

    P = sorted(P, key=lambda v: v.y, reverse=True)  # sortowanie punktów

    stack = []
    stack.append(P[0])  # wrzucenie na stosu dwóch pierwszych punktów
    stack.append(P[1])
    scenes = []
    diagonals = []  # lista krawędzi wyrażonych floatami, do rysowania kolejnych scen
    diagonals_by_indexes = []  # zwracana lista indeksów punktów między którymi ą krawędzie

    for i in range(2, n):
        if P[i].chain != stack[-1].chain:  # jeśli dwa nie punkty są na tym samym łańcuchu
            first = stack[-1]
            while len(stack) > 1:
                top = stack.pop()
                if do_not_follow(P[i], top, n):  # jeśli jeszcze nie ma krawędzi między tymi punktami
                    diagonals.append((P[i].get_coords(), top.get_coords()))
                    diagonals_by_indexes.append((P[i].index, top.index))

            stack.pop()
            stack.append(first)
        else:  # jeśli dwa punkty są na tym samym łańcuchu
            top = stack.pop()
            top_prev = stack.pop()
            while inside_polygon(P[i].get_coords(), top.get_coords(), top_prev.get_coords(),
                                 P[i].chain):  # dopóki trójkąt tworzony przez t punkty jest wewnątrz wielokąta
                if do_not_follow(P[i], top_prev, n):  # jeśli jeszce nie ma kraedzi między tymi punktami
                    diagonals.append((P[i].get_coords(), top_prev.get_coords()))
                    diagonals_by_indexes.append((P[i].index, top_prev.index))

                if not len(stack):
                    stack = stack + [top_prev]
                    break
                top, top_prev = top_prev, stack.pop()
            else:
                stack = stack + [top_prev, top]
        stack.append(P[i])

    return diagonals_by_indexes

x.runtest(3, triangulate)

# end ---------------------------------------------------------------------------------------------------------
"""
# budziak
"""
# task 1 test --------------------------------------------------------------------------------------------------------
def det(a, b, c):
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    first = (a_x - c_x) * (b_y - c_y)
    second = (a_y - c_y) * (b_x - c_x)
    determinant = first - second
    return determinant

def connective_or_separative(a, b, c, epsilon=10 ** (-12)):
    determinant = det(a, b, c)
    if a[1] > b[1] and c[1] > b[1] and determinant < -epsilon:
        return True
    elif a[1] < b[1] and c[1] < b[1] and determinant < -epsilon:
        return True
    return False

def y_monotonic(points):
    for i in range(0, len(points) - 1):
        if connective_or_separative(points[i - 1], points[i], points[i + 1]):
            return False

    if connective_or_separative(points[-2], points[-1], points[0]):
        return False
    return True


x = Test()
x.runtest(1, y_monotonic)

# task 2 test --------------------------------------------------------------------------------------------------------
def classify(a, b, c, starting, closing, connective, separative, correct, n, epsilon=10 ** (-12)):
    # starting or separative or correct
    if a[1] < b[1] and c[1] < b[1]:
        # starting
        if det(a, b, c) > epsilon:
            starting.append(n)
        # separative
        elif det(a, b, c) < -epsilon:
            separative.append(n)

    # closing or connective or correct
    elif a[1] > b[1] and c[1] > b[1]:
        # closing
        if det(a, b, c) > epsilon:
            closing.append(n)
        # connective
        elif det(a, b, c) < -epsilon:
            connective.append(n)

    # correct
    else:
        correct.append(n)

def classify_points(points):
    starting = []
    closing = []
    connective = []
    separative = []
    correct = []
    # all points excep first and last
    for i in range(0, len(points) - 1):
        classify(points[i - 1], points[i], points[i + 1], starting, closing, connective, separative, correct, i)

    # last point
    classify(points[-2], points[-1], points[0], starting, closing, connective, separative, correct, len(points)-1)

    result = [-1]*len(points)
    for i in starting:
        result[i] = 0
    for i in closing:
        result[i] = 1
    for i in connective:
        result[i] = 2
    for i in separative:
        result[i] = 3
    for i in correct:
        result[i] = 4

    return result

x.runtest(2, classify_points)

# task 3 test --------------------------------------------------------------------------------------------------------
def find_chains(points):
    right_chain = set()
    left_chain = set()
    starting = points.index(max(points, key=lambda x: x[1]))
    ending = points.index(min(points, key=lambda x: x[1]))
    i = ending
    while i != starting:
        right_chain.add(points[i])
        i = (i + 1) % len(points)
    while i != ending:
        left_chain.add(points[i])
        i = (i + 1) % len(points)
    return left_chain, right_chain


def check_same_chains(left_chain, right_chain, point1, point2):
    if (point1 in left_chain and point2 in left_chain) or (point1 in right_chain and point2 in right_chain):
        return True
    return False

def triangle_in_polygon(chain, a, b, c, epsilon=10 ** (-12)):
    if b in chain:
        return det(a, b, c) > epsilon
    else:
        return det(a, b, c) < -epsilon


def check_neighbours(points, a, b):
    a_index = points.index(a)
    b_index = points.index(b)
    if abs(a_index - b_index) == 1:
        return True
    elif abs(a_index - b_index) == len(points) - 1:
        return True
    return False

def tup_points(points):
    return [tuple(point) for point in points]

def triangulation(points):
    if not y_monotonic(points):
        return None
    points = tup_points(points)
    points_copy = points[:]
    left_chain, right_chain = find_chains(points)
    points.sort(key=lambda x: x[1], reverse=True)

    stack = [points[0], points[1]]
    diagonals = []
    for i in range(2, len(points)):
        if not check_same_chains(left_chain, right_chain, stack[-1], points[i]):
            while len(stack) > 0:
                p = stack.pop()
                if not check_neighbours(points_copy, p, points[i]):
                    diagonals.append((points_copy.index(points[i]), points_copy.index(p)))

            stack.append(points[i - 1])
            stack.append(points[i])
        else:
            p = stack.pop()
            while len(stack) > 0 and triangle_in_polygon(left_chain, stack[-1], p, points[i]):
                if not check_neighbours(points_copy, p, points[i]) and \
                        (points[i], p) not in diagonals:
                    diagonals.append((points_copy.index(points[i]), points_copy.index(p)))
                if not check_neighbours(points_copy, stack[-1], points[i]) and \
                        (points[i], stack[-1]) not in diagonals:
                    diagonals.append((points_copy.index(points[i]), points_copy.index(stack[-1])))
                p = stack.pop()

            stack.append(p)
            stack.append(points[i])

    return diagonals

x.runtest(3, triangulation)
# end ---------------------------------------------------------------------------------------------------------
"""