class TestCore:
    def __init__(self):
        self.tests_in = [[-1, -1, -1, -1],  # number of tests in [lab-1 = row][task-1 = column]
                         [-1, -1, -1, -1],  # lab 2
                         [3, 3, 3],      # lab 3
                         [-1, -1, -1, -1]]  # lab 4
    # ewentualnie /\ to /\ można usunąć i zrobić na podstawie ilości plików w folderach, ale wtedy trzeba
    # się dogadać jak ma wyglądać budowa drzewo folderów (przykład na branch'u lab_3_tests, implementacja niżej w """).

    def test(self, lab_no, task_no, test_func, func):
        print("Lab {}, task {}:".format(lab_no, task_no))

        counter = 0
        for test_no in range(1, self.tests_in[lab_no - 1][task_no - 1] + 1):
            print("\tTest {}:".format(test_no), end=" ")

            result, output, expected = test_func(test_no, func)

            if result == 1:
                print("Passed")
                counter += 1
            else:
                print("WRONG ANSWER")
                print("\t\tOutput:   {}".format(output))
                print("\t\tExpected: {}".format(expected))
                
        """
        from os import listdir
        counter = 0
        for test_no in range(1, len(listdir("test{}_tests\\task{}".format(lab_no, task_no)))//2 + 1):
            print("\tTest {}:".format(test_no), end=" ")

            result, output, expected = test_func(test_no, func)

            if result == 1:
                print("Passed")
                counter += 1
            else:
                print("WRONG ANSWER")
                print("\t\tOutput: {}".format(output))
                print("\t\tExpected: {}".format(expected))
                
        """

        print("Result: {}/{}\n".format(counter, self.tests_in[lab_no - 1][task_no - 1]))
