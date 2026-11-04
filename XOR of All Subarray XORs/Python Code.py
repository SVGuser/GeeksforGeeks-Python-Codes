class Solution:
    def subarrayXor(self, arr):
        y = len(arr)
        if y % 2 == 0:
            return 0
        res = 0
        for i in range(0, y, 2):
            res ^= arr[i]
        return res
