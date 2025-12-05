#User function Template for python3

class Solution:
    def rotate(self, arr):
    
     def reverse(start,end):
        while (start<end):
            arr[start],arr[end]=arr[end],arr[start]
            start += 1
            end -= 1
     reverse(0,len(arr)-2)
     reverse(len(arr)-1,len(arr)-1)
     reverse(0,len(arr)-1)
     
    
     return arr
        
