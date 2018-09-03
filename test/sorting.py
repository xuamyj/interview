from code.sorting.merge_sort import MergeSort
from code.sorting.quick_sort import QuickSort

class SortingTester(object):
    def __init__(self):
        pass

    def runTest(self, testName):
        if testName == 'merge_sort':
            self.runMergeSortTests()
        elif testName == 'quick_sort':
            self.runQuickSortTests()

    def runMergeSortTests(self):
        sortObj = MergeSort()
        self.verifySort(sortObj)

    def runQuickSortTests(self):
        sortObj = QuickSort()
        self.verifySort(sortObj)

    def verifySort(self, sortObj):
        arrays = [
            [], # 0 elems
            [0], # 1 elems
            [-20],
            [-1, 1], # 2 elems, forward
            [2, -2], # 2 elems, backward
            [3, 3], # 2 elems, duplicate
            [5, 4, 4], # 3 elems
            [4, 2, 5],
            [1, 2, 3],
            [9, 7, 4, 0, 8, 3, 2, 7, 8, 7], # many even
            [5, 5, 4, 7, 6, 6, 0, 1, 2], # many odd
            [1, 1, 1, 1, -5, -5, -5], # duplicates
            [9, 8, 7, 6, 5 ,4, 3], # reverse
        ]

        for arr in arrays:
            print 'Sorting', arr
            assert sortObj.sorted(arr) == sorted(arr)
        print 'Passed all %s tests.' % (sortObj.name)
