class Solution:
	def twoSum(self, arr, target):
	    d={}
	    for i in range(0,len(arr)):
	        v = arr[i]
	        diff = target - v
	        
	        if v not in d:
	            d[diff]=i
	        else:
	            current_index=i
	            previous_index = d[v]
	            return previous_index, current_index
	        
