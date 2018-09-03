import random

class QuickSort(object):
    def __init__(self):
        self.name = 'quick_sort'

    def swap(self, arr, indexA, indexB):
        temp = arr[indexA]
        arr[indexA] = arr[indexB]
        arr[indexB] = temp

    # Sorting [9, 7, 4, 0, 8, 3, 2, 7, 8, 7]
    # 0 0 9 pivotVal= 9
    # [7, 7, 4, 0, 8, 3, 2, 7, 8, 9]
    # 0 2 7 pivotVal= 4
    # [2, 3, 0, 4, 8, 7, 7, 7, 8, 9]
    # 0 2 2 pivotVal= 0
    # [2, 3, 0, 4, 8, 7, 7, 7, 8, 9]
    # 1 2 2 pivotVal= 0
    # [2, 3, 0, 4, 8, 7, 7, 7, 8, 9]
    # 4 4 7 pivotVal= 8
    # [2, 3, 0, 4, 7, 7, 7, 8, 8, 9]
    # 4 4 5 pivotVal= 7
    # [2, 3, 0, 4, 7, 7, 7, 8, 8, 9]
    # [2, 3, 0, 4, 7, 7, 7, 8, 8, 9]

    def quickHelper(self, arr, leftIndex, rightIndex):
        if (leftIndex >= rightIndex):
            return

        origLeftIndex = leftIndex
        origRightIndex = rightIndex

        # get pivot
        origPivotIndex = random.randint(leftIndex, rightIndex)
        pivotVal = arr[origPivotIndex]

        while leftIndex < rightIndex:
            if arr[leftIndex] < pivotVal:
                leftIndex += 1
            elif arr[rightIndex] >= pivotVal:
                rightIndex -= 1
            else:
                self.swap(arr, leftIndex, rightIndex)
                leftIndex += 1 # amy says: is this not trusting the recursion or optimization?
                rightIndex -= 1

        print origLeftIndex, origPivotIndex, origRightIndex, 'pivotVal=', pivotVal
        print arr

        # at this point, leftIndex == rightIndex
        self.quickHelper(arr, origLeftIndex, leftIndex - 1)
        self.quickHelper(arr, leftIndex + 1, origRightIndex)

    def sorted(self, arr):
        copy = arr[:]
        self.quickHelper(copy, 0, len(arr)-1)
        print copy
        return copy

