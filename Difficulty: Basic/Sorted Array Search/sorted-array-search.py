#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        l = 0
        r = len(arr)-1
        while l<=r:
            m = (l+r)//2
            if k == arr[m] :
                return True 
            elif k > arr[m] :
                l = m + 1
            elif k < arr[m] :
                r = m -1
        return False
    