class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k >= n:
            return 0
        
        # Precompute prefix max and min
        max_pref, min_pref = [0] * n, [0] * n
        max_pref[0] = min_pref[0] = arr[0]
        for i in range(1, n):
            max_pref[i] = max(max_pref[i-1], arr[i])
            min_pref[i] = min(min_pref[i-1], arr[i])
            
        # Precompute suffix max and min
        max_suf, min_suf = [0] * n, [0] * n
        max_suf[n-1] = min_suf[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            max_suf[i] = max(max_suf[i+1], arr[i])
            min_suf[i] = min(min_suf[i+1], arr[i])
            
        res = float('inf')
        
        # Evaluate each possible subarray of length k to remove
        for i in range(n - k + 1):
            max_cur = float('-inf')
            min_cur = float('inf')
            
            # Incorporate elements before the removed window
            if i > 0:
                max_cur = max(max_cur, max_pref[i-1])
                min_cur = min(min_cur, min_pref[i-1])
                
            # Incorporate elements after the removed window
            if i + k < n:
                max_cur = max(max_cur, max_suf[i+k])
                min_cur = min(min_cur, min_suf[i+k])
                
            res = min(res, max_cur - min_cur)
            
        return res
