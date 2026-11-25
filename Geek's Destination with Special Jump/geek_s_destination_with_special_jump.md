# Geek's Destination with Special Jump

**Platform:** GeeksforGeeks  
**Problem Link:** [Geek's Destination with Special Jump](https://www.geeksforgeeks.org/problems/geek-and-her-destination--145724/1)  
**Language:** Python 3  
**Time Taken:** 0.04s  
**Status:** Solved (1120 / 1120 Test Cases Passed)

---

## Approach & Intuition

The problem requires finding the sum of minimum times needed to reach a destination $d$ starting from every position $c$ in the range $[l, r]$, modulo $10^9 + 7$.

1. **Minimum Time for a Single Position (`timeJump(c)`):**
   - Let $\text{rem} = d - c$ be the remaining distance.
   - If $\text{rem} \le 0$, Geek is already at or past the destination, taking $1$ unit of time (or the base step).
   - If $\text{rem} \le a$, Geek can reach the destination directly without slipping back, taking $\text{rem} + 1$ time.
   - Otherwise, in each full cycle of moving forward $a$ and slipping back $b$, Geek makes a net progress of $\text{net} = a - b$. The number of full cycles required before the final push is $\lceil \frac{\text{rem} - a}{\text{net}} \rceil$. Each cycle adds $2b$ extra time on top of the base distance $\text{rem} + 1$.

2. **Prefix Sum Optimization (`prefix(t)` & `sum_up(t)`):**
   - Since $[l, r]$ can be very large, iterating over each $c \in [l, r]$ is too slow.
   - Instead, we observe that as $c$ decreases (moving further away from $d$), the required time $t$ increases monotonically.
   - Using `t1 = timeJump(l)` and `t2 = timeJump(r + 1)`, we transform the range query over positions $[l, r]$ into a range query over time thresholds $[t_2 + 1, t_1]$.
   - `prefix(t)` calculates the total sum of valid starting positions for all time steps up to $t$ by subtracting the "dead" time steps (where Geek is slipping backward, computed via arithmetic progression in `sum_up(t)`) from the total sum $\frac{t(t+1)}{2} \pmod{10^9 + 7}$.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ — All calculations rely on constant-time arithmetic progressions and modular inverse multiplication.
- **Space Complexity:** $\mathcal{O}(1)$ — Only a few integer variables are used.

---

## Solution Code

```python
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
```

---

## Git Commit Message

```text
feat(gfg): solve Geek's Destination with Special Jump in O(1) time

- Implement timeJump() to compute minimum time from a given start point
- Use prefix sums and arithmetic progression to evaluate range [l, r] in O(1)
- Handle modular arithmetic under 10^9 + 7
```