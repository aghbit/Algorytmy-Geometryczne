from os import path, listdir
from bitalg import __path__ as pkg_path


def get_test_path(lab_no, task_no, test_no):
    return path.join(pkg_path[0], f"tests/test{lab_no}_tests/task{task_no}/test_{lab_no}_{task_no}_{test_no}")


class TestCore:
    def __init__(self):
        self.tests_in = [[4, 2],  # number of tests in [lab-1 = row][task-1 = column]
                         [11, 11],  # lab 2
                         [10, 10, 10],  # lab 3
                         [1, 3]]  # lab 4

    def test(self, lab_no, task_no, test_func, func, *args):
        print("Lab {}, task {}:".format(lab_no, task_no))

        if lab_no == 1:
            limit = self.tests_in[lab_no - 1][task_no - 1] + 1
        else:
            limit = len(listdir(path.join(pkg_path[0], f"tests/test{lab_no}_tests/task{task_no}"))) // 2 + 1

        counter = 0
        for test_no in range(1, limit):
            print("\tTest {}:".format(test_no), end=" ")

            result, *output_expected = test_func(test_no, func, *args)

            if result == 1:
                print("Passed")
                counter += 1
            else:
                print("WRONG ANSWER")
                print("\t\tOutput:   {}".format(output_expected[0]))
                print("\t\tExpected: {}".format(output_expected[1]))

        print("Result: {}/{}".format(counter, self.tests_in[lab_no - 1][task_no - 1]))
