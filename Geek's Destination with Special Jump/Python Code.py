import math
class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        mid = (MOD + 1) // 2
        def timeJump(c: int) -> int:
            rem = d - c
            if rem <= 0:
                return 1
            if rem <= a:
                return rem + 1
            net = a - b
            cycles = (rem - a + net - 1) // net
            return rem + 2 * b * cycles + 1
        def sum_up(t: int) -> int:
            first = a + 2
            timer = a + b
            if t < first:
                return 0
            cnt = (t - first) // timer + 1
            last = first + (cnt - 1) * timer
            term1 = (b % MOD) * (cnt % MOD) % MOD
            term1 = term1 * ((first + last) % MOD) % MOD
            term2 = (cnt % MOD) * ((2 * b - 1) % MOD) % MOD
            term2 = term2 * ((2 * b) % MOD) % MOD
            term2 = term2 * mid % MOD
            return (term1 + term2) % MOD
        def prefix(t: int) -> int:
            overall = (t % MOD) * ((t + 1) % MOD) % MOD
            overall = overall * mid % MOD
            return (overall - sum_up(t) + MOD) % MOD
        t1 = timeJump(l)
        t2 = timeJump(r + 1)
        return (prefix(t1) - prefix(t2) + MOD) % MOD
