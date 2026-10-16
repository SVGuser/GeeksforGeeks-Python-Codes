class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        suffix = [0] * n
        curr = float('inf')
        for i in range(n - 1, -1, -1):
            curr = min(curr, arr[i])
            suffix[i] = curr
        cnt = 0
        left = float('-inf')
        for i in range(n):
            if arr[i] > left and arr[i] == suffix[i]:
                cnt += 1
            left = max(left, arr[i])
        return cnt
