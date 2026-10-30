class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        val_max = max(n, max(arr)) if arr else n
        frq = [0] * (val_max + 1)
        power = [1] * (n + 1)
        for x in arr:
            frq[x] += 1
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % MOD
        curr = 1
        start = 0
        ans = 0
        for k in range(val_max + 1):
            start += frq[k] if k <= n else 0
            if l <= k <= r and k <= n:
                ways = (curr * power[n - start]) % MOD
                ans = (ans + ways) % MOD
            if k <= n:
                frq_k = frq[k]
                curr = (curr * (power[frq_k] - 1 - MOD)) % MOD
        return ans
