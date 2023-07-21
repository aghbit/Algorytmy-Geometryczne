class TestCore:
    def __init__(self):
        self.tests_in = [[-1, -1, -1, -1],  # number of tests in [lab-1 = row][task-1 = column]
                         [-1, -1, -1, -1],  # lab 2
                         [ 2, -1, -1, -1],  # lab 3
                         [-1, -1, -1, -1]]  # lab 4
    # ewentualnie /\ to /\ można usunąć i zrobić na podstawie ilości plików w folderach, ale wtedy trzeba
    # się dogadać jak ma wyglądać budowa drzewo folderów.

    def test(self, lab_no, task_no, func):
        print("Lab " + str(lab_no) + str(", task ") + str(task_no) + ":")

        for test_no in range(1, self.tests_in[lab_no - 1][task_no - 1] + 1):
            print("\tTest: " + str(test_no), end=": ")

            result = func(lab_no, task_no, test_no)

            if result:
                print("Passed")
            else:
                print("WRONG ANSWER")
