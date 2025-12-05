#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        i = j = 0
        n, m = len(a), len(b)
        while j < m and i < n:
            if a[i] < b[j]:
                i += 1
            elif a[i] == b[j]:
                i += 1
                j += 1
            else: 
                return False
        return j == m  

    
    
    
    
    
