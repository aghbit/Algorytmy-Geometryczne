from .test_core import TestCore, get_test_path

class Point:
    def __init__(self, x_cord, y_cord, eps):
        self.x = x_cord
        self.y = y_cord
        self.eps = eps

    def __eq__(self, other):
        if abs(self.x - other.x) < self.eps:
            return True
        return False

    def __hash__(self):
        return hash(self.x)

    def __str__(self):
        return f"{self.x} | {self.y} | {self.eps}"


class Test(TestCore):
    def runtest(self, task_no, func, eps=10**(-12)):
        if task_no == 1:
            TestCore.test(self, 4, 1, self.task1_fun, func, eps)
        elif task_no == 2:
            TestCore.test(self, 4, 2, self.task2_func, func, eps)
        elif task_no == 3:
            TestCore.test(self, 4, 3, self.task3_fun, func, eps)

    @staticmethod
    def read_data(task_no, test_no):
        """
        :param task_no:
        :param test_no:
        :return:
        """
        points = []
        try:
            with open(get_test_path(4, task_no, test_no) + ".in") as file:
                for point in file:
                    points.append(list(map(float, point.split(" "))))
            return points
        except FileNotFoundError:
            print(f"ERROR: File not found ({get_test_path(4, task_no, test_no)}.in)")
            return []

    @staticmethod
    def read_points(task_no, test_no):
        """
        :param task_no:
        :param test_no:
        :return:
        """
        lines = []
        with open(get_test_path(4, task_no, test_no) + ".in") as file:
            for point in file:
                x1, y1, x2, y2 = (map(float, point.split(" ")))
                lines.append(((x1, y1), (x2, y2)))
        return lines

    def task1_fun(self, test_no, func, eps):
        """
        :param test_no:
        :param func:
        :param eps:
        :return:
        """
        try:
            with open(get_test_path(4, 1, test_no) + ".in") as file:
                max_x, max_y, n = file.read().split("\n")
            return self.task1_checker(func, max_x, max_y, n, eps)

        except FileNotFoundError:
            print(os.getcwd())
            print(f"ERROR: File not found ({get_test_path(4, 1, test_no)}.in)")
            return []

    @staticmethod
    def task1_checker(func, max_x, max_y, n, eps):
        """
        :param func:
        :param max_x:
        :param max_y:
        :param n:
        :param eps:
        :return:
        """
        max_x = float(max_x)
        max_y = float(max_y)
        n = int(n)
        sections = func(max_x, max_y, n)
        # print(sections)
        if len(sections) != n:
            return 0, len(sections), f"{n}  || generujesz złą liczbę odcinków"
        ends = set()
        for i in range(len(sections)):
            start = sections[i][0]
            end = sections[i][1]
            ends.add(Point(start[0], start[1], eps))
            ends.add(Point(end[0], end[1], eps))
            if abs(start[0]-end[0]) < eps:
                return 0, f"punkt początkowy ma współrzędną {start[0]}", f"a końcowy {end[0]}  || linia numer {i} zaczyna i kończy się w tej samej współrzędnej x "
            if max_x < start[0]:
                return 0, f"współrzędna x wynosi {start[0]}", f"górna granica przedziału wynosi {max_x} || współrzędna większa niż górna granica przedziału "
            if max_y < start[1]:
                return 0, f"współrzędna y wynosi {start[1]}", f"górna granica przedziału wynosi {max_y} || współrzędna większa niż górna granica przedziału"
            if max_x < end[0]:
                return 0,f"współrzędna x wynosi {end[0]}", f"górna granica przedziału wynosi {max_x} || współrzędna większa niż górna granica przedziału"
            if max_y < end[1]:
                return 0,f"współrzędna y wynosi {end[1]}", f"górna granica przedziału wynosi {max_y} || współrzędna większa niż górna granica przedziału"
            if 0 > start[0]:
                return 0,f"współrzędna x wynosi {start[0]}", f"dolna granica wprzedziału wynosi 0 || współrzędna mniejsza niż dolna granica przedziału"
            if 0 > start[1]:
                return 0,f"współrzędna x wynosi {start[1]}", f"dolna granica wprzedziału wynosi 0 || współrzędna mniejsza niż dolna granica przedziału"
            if 0 > end[0]:
                return 0, f"współrzędna x wynosi {end[0]}", f"dolna granica wprzedziału wynosi 0 || współrzędna mniejsza niż dolna granica przedziału"
            if 0 > end[1]:
                return 0, f"współrzędna x wynosi {end[1]}", f"dolna granica wprzedziału wynosi 0 || współrzędna mniejsza niż dolna granica przedziału"
        if len(ends) != n*2:
            return 0, f"unikalnych końców jest {len(ends)}", f"unikalnych końców powinno byc {n*2}  || jakiś odcinek zaczyna i kończy się w tym samym miejscu"
        return 1, None

    def task2_func(self, test_no, func, eps):
        """
        :param test_no:
        :param func:
        :return:
        """
        test_data = self.read_points(2, test_no)
        output = False if open(get_test_path(4, 2, test_no) + ".out").read() == "0" else True
        result = func(test_data)
        if result == output:
            return 1, None
        return 0, result, output

    @staticmethod
    def list_to_dictionary(input_list: list, eps: float):
        output_dict = {}
        for intersection in input_list:
            if type(intersection) == str:
                intersection_val = intersection.split(" ")
                x, y, id1, id2 = intersection_val[0], intersection_val[1], int(intersection_val[2]), int(intersection_val[3])
                point = Point(float(x), float(y), eps)
            else:
                point, id1, id2 = intersection[0], intersection[1], intersection[2]
                point = Point(point[0], point[1], eps)
            key = (min(id1, id2), max(id1, id2))
            output_dict[key] = point
        return output_dict

    def task3_fun(self, test_no, func, eps):
        """
        :param test_no:
        :param func:
        :param eps:
        :return:
        """
        test_data = self.read_points(3, test_no)
        output = open(get_test_path(4, 3, test_no) + ".out").read().split('\n')
        result = func(test_data)
        if len(output) == 1 and output[0] == "":
            if not result:
                return 1, None
            else:
                return 0, result, output

        output_dict = self.list_to_dictionary(output, eps)
        result_dict = self.list_to_dictionary(result, eps)
        if output_dict == result_dict:
            return 1, None
        return 0, result, output
