class Solution:
    def getMinMax(self, arr):
        arr.sort()
        return arr[0],arr[-1]