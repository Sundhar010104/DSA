class Solution:
    def countTriplet(self, arr):
        n = len(arr)
        arr.sort()
        count = 0

        # Fix arr[k] as the largest element of the triplet
        for k in range(n - 1, -1, -1):   # or range(n - 1, 1, -1) is also fine
            i = 0
            j = k - 1

            # Two-pointer search for pairs (i, j) such that arr[i] + arr[j] == arr[k]
            while i < j:
                s = arr[i] + arr[j]
                if s == arr[k]:
                    count += 1
                    i += 1
                    j -= 1
                elif s < arr[k]:
                    i += 1
                else:  # s > arr[k]
                    j -= 1

        return count
