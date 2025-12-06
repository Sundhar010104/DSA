class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        if n < 3:
            return False

        for i in range(n - 2):
            # skip duplicate 'i' values (check i>0 first)
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                if s == target:
                    return True

                if s < target:
                    l += 1
                    # skip duplicates safely (check bounds first)
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
                else:  # s > target
                    r -= 1
                    # skip duplicates safely (check bounds first)
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1

        # no triplet found after checking all i
        return False

                    
        