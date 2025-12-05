class Solution:
    def thirdLargest(self,arr):
        arr.sort()
        y = arr[-3]
        return y
        