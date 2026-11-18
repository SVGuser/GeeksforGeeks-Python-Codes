# Find XOR of Numbers from L to R

## Problem Statement

Given two integers `l` and `r`, find the bitwise XOR of all integers in the inclusive range $[l, r]$:

$$
l \oplus (l + 1) \oplus (l + 2) \oplus \dots \oplus r
$$

### Constraints

* $1 \le l \le r \le 10^9$ (also handles $l = 0$ safely)

### Examples

**Example 1:**

```text
Input: l = 4, r = 8
Output: 8
Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
```

**Example 2:**

```text
Input: l = 3, r = 7
Output: 3
Explanation:
3 ^ 4 ^ 5 ^ 6 ^ 7 = 3
```

## Explanation & Intuition

1. **Prefix XOR Property:**
   Because the XOR operation is its own inverse ($x \oplus x = 0$) and is both associative and commutative, the XOR of a range $[l, r]$ can be computed from prefix XORs starting at $0$:

   $$
   \text{XOR}(l, r) = \text{XOR}(0, r) \oplus \text{XOR}(0, l - 1)
   $$

   All elements from $0$ to $l - 1$ appear twice and cancel each other out, leaving only the elements from $l$ to $r$.

2. **Modulo-4 Pattern for** $\text{XOR}(0, n)$**:**
   Computing $\text{XOR}(0, n)$ directly for small values reveals a repeating 4-step pattern based on $n \pmod 4$:

   * $n = 0 \implies 0$ ($n \equiv 0 \pmod 4 \rightarrow n$)
   * $n = 1 \implies 0 \oplus 1 = 1$ ($n \equiv 1 \pmod 4 \rightarrow 1$)
   * $n = 2 \implies 1 \oplus 2 = 3$ ($n \equiv 2 \pmod 4 \rightarrow n + 1$)
   * $n = 3 \implies 3 \oplus 3 = 0$ ($n \equiv 3 \pmod 4 \rightarrow 0$)
   * $n = 4 \implies 0 \oplus 4 = 4$ ($n \equiv 0 \pmod 4 \rightarrow n$)

   This pattern holds for all non-negative integers because any block of 4 consecutive numbers starting at a multiple of 4 ($4k, 4k+1, 4k+2, 4k+3$) has a combined XOR of $0$.

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(1)$

  Both `totalXOR(r)` and `totalXOR(l - 1)` perform a constant number of arithmetic and bitwise operations regardless of how large $l$ and $r$ are.

* **Space Complexity:** $\mathcal{O}(1)$

  No extra data structures or recursive call stacks are required.

## Implementation & Unit Testing

Below is the complete Python 3 implementation along with a `unittest` suite covering standard ranges, single-element bounds, zero-indexed ranges, and large constraints:

```python
import unittest


class Solution:
    def findXOR(self, l: int, r: int) -> int:
        # Helper function to compute the XOR of all numbers from 0 to n
        def totalXOR(n: int) -> int:
            # Base case for negative bounds (e.g., when l = 0, l - 1 = -1)
            if n < 0:
                return 0
            
            # The cumulative XOR from 0 to n follows a strict cycle of length 4
            rem = n % 4
            if rem == 0:
                return n
            elif rem == 1:
                return 1
            elif rem == 2:
                return n + 1
            else:
                return 0
                
        # Use prefix XOR property: XOR(l..r) = XOR(0..r) ^ XOR(0..l-1)
        return totalXOR(r) ^ totalXOR(l - 1)


class TestFindXOR(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard_ranges(self):
        # 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
        self.assertEqual(self.sol.findXOR(4, 8), 8)
        # 3 ^ 4 ^ 5 ^ 6 ^ 7 = 3
        self.assertEqual(self.sol.findXOR(3, 7), 3)

    def test_single_element_range(self):
        # When l == r, result should be the element itself
        self.assertEqual(self.sol.findXOR(5, 5), 5)
        self.assertEqual(self.sol.findXOR(12, 12), 12)

    def test_zero_start_range(self):
        # 0 ^ 1 ^ 2 ^ 3 = 0
        self.assertEqual(self.sol.findXOR(0, 3), 0)
        # 0 ^ 1 ^ 2 = 3
        self.assertEqual(self.sol.findXOR(0, 2), 3)

    def test_large_constraints(self):
        # 10^9 is divisible by 4, so XOR(0..10^9) = 10^9; XOR(0..0) = 0
        self.assertEqual(self.sol.findXOR(1, 10**9), 10**9)


if __name__ == "__main__":
    unittest.main()
```