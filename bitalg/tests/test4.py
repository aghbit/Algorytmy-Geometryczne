from bitalg.tests.test_core import TestCore, get_test_path


class Test(TestCore):
    def __init__(self):
        super().__init__()

    def runtest(self, task_no, func):
        if task_no == 1:
            TestCore.test(self, 4, 1, self.task1_func, func)
        elif task_no == 2:
            TestCore.test(self, 4, 2, self.task2_func, func)

    @staticmethod
    def read_data(task_no, test_no):
        """

        :param task_no:
        :param test_no:
        :return:
        """
        points = []
        with open(get_test_path(4, task_no, test_no) + ".in") as file:
            for point in file:
                points.append(list(map(float, point.split(" "))))
        return points

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
                lines.append([(x1, y1), (x2, y2)])
        return lines

    def task1_func(self, test_no, func):
        """

        :param test_no:
        :param func:
        :return:
        """
        test_data = self.read_data(1, test_no)
        output = open(get_test_path(4, 1, test_no) + ".out").read()
        result = func(test_data[0], test_data[1], test_data[2])
        if str(result) == output:
            return 1, None
        return 0, result, output

    @staticmethod
    def list_to_dictionary(input_list: list):
        output_dict = {}
        for intersection in input_list:
            # TODO dorobić try catch
            line1, line2 = intersection.split(" ")[0], intersection.split[1]
            output_dict[min(line1, line2)] = [max(line1, line2)] + [*output_dict[min(line1, line2)]]
        for val in output_dict.values():
            val.sort()
        return output_dict

    def task2_func(self, test_no, func):
        """

        :param test_no:
        :param func:
        :return:
        """
        test_data = self.read_points(1, test_no)
        output = open(get_test_path(4, 2, test_no) + ".out").read().split('\n')
        result = func(test_data)
        # TODO co ma user zwracać? na razie zakładam, że same indeksu przecięć
        # TODO pytanie czy to rozbić na dwa testy jeden na liczbę przecięć, drugi na to które z którym się przecinają
        if len(result) != int(output[0]):
            return 0, result, output

        output_dict = self.list_to_dictionary(output[1:])
        result_dict = self.list_to_dictionary(result)
        if output_dict == result_dict:  # TODO czy to serio zadziała?
            return 1, None
        return 0, result, output
