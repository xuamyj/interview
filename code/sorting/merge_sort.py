class MergeSort(object):
    def __init__(self):
        self.name = 'merge_sort'

    def mergeHelper(self, arr):
        # base case
        if len(arr) <= 1: # amy says: huh has to be 1 not 0
            return arr

        # recurse on each half
        midIndex = len(arr)/2
        leftArr = self.mergeHelper(arr[:midIndex])
        rightArr = self.mergeHelper(arr[midIndex:])

        # init for merge
        result = [0]*(len(leftArr) + len(rightArr))
        index = 0
        leftIndex = 0
        rightIndex = 0

        # merge
        while index < len(result):
            if leftIndex >= len(leftArr): # use rest of right
                result[index:] = rightArr[rightIndex:]
                break
            elif rightIndex >= len(rightArr): # use rest of left
                result[index:] = leftArr[leftIndex:]
                break
            elif leftArr[leftIndex] < rightArr[rightIndex]: # left comes first
                result[index] = leftArr[leftIndex]
                index += 1
                leftIndex += 1
            else: # right comes first
                result[index] = rightArr[rightIndex]
                index += 1
                rightIndex += 1

        return result

    def sorted(self, arr):
        return self.mergeHelper(arr)
