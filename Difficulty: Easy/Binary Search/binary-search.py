class Solution:
    def binarysearch(self, arr, k):
        l = 0
        r = len(arr)-1
        ans = -1
        while l<=r:
            m = (l+r)//2
            if k == arr[m] :
                ans = m
                r = m - 1
            elif k > arr[m] :
                l = m + 1
            elif k < arr[m] :
                r = m -1
        return ans
    
        