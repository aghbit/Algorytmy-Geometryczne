class TestCore:
    def __init__(self):
        self.tests_in = [[-1, -1, -1, -1],  # number of tests in [lab-1 = row][task-1 = column]
                         [-1, -1, -1, -1],  # lab 2
                         [ 2, -1, -1, -1],  # lab 3
                         [-1, -1, -1, -1]]  # lab 4
    # ewentualnie /\ to /\ można usunąć i zrobić na podstawie ilości plików w folderach, ale wtedy trzeba
    # się dogadać jak ma wyglądać budowa drzewo folderów.

    def test(self, lab_no, task_no, func):
        print("Lab {}, task {}:".format(lab_no, task_no))

        counter = 0
        for test_no in range(1, self.tests_in[lab_no - 1][task_no - 1] + 1):
            print("\tTest {}:".format(test_no), end=" ")

            result = func(lab_no, task_no, test_no)

            if result == 1:
                print("Passed")
                counter += 1
            #elif result == 0:
            #    print("TIMEOUT")
            else:
                print("WRONG ANSWER")

        print("Result {}/{}".format(counter, self.tests_in[lab_no - 1][task_no - 1]))

def m(lab, task, test):
    res = 1
    list = open("test{}_tests\\task{}\\test_{}_{}_{}.in".format(lab, task, lab, task, test), "r").read().split(" ")
    for i in list:
        res *= int(i)
    if str(res) == open("test{}_tests\\task{}\\test_{}_{}_{}.out".format(lab, task, lab, task, test), "r").read():
        return True
    else:
        return False

x = TestCore()
x.test(3,1,m)

