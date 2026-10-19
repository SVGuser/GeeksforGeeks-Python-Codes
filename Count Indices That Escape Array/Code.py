class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        new = [0] * n
        def dfs(i: int) -> bool:
            if i < 0 or i >= n:
                return True
            if new[i] == 1:
                return False
            if new[i] == 2:
                return True
            if new[i] == 3:
                return False
            if arr[i] == 0:
                new[i] == 3
                return False
            new[i] = 1
            new_idx = i + arr[i]
            if dfs(new_idx):
                new[i] = 2
                return True
            else:
                new[i] = 3
                return False
        good_cnt = 0
        for i in range(n):
            if new[i] == 0:
                dfs(i)
            if new[i] == 2:
                good_cnt += 1
        return good_cnt
