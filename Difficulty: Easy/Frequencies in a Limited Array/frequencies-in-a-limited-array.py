class Solution:
    def frequencyCount(self, arr):
        hash = [0]*len(arr)
        for i in arr:
            hash[i-1]+=1
        return hash

