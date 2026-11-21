# Smallest Subarray with Sum Greater Than X

## Problem Statement

Given an array of positive integers `arr` and a number `x`, find the length of the smallest contiguous subarray whose sum is strictly greater than `x`. If no such subarray exists, return `0`.

### Constraints

* $1 \le \text{arr.length} \le 10^5$
* $1 \le \text{arr}[i] \le 10^4$
* $1 \le x \le 10^9$

### Examples

**Example 1:**

```text
Input: x = 51, arr = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation:
Minimum length subarray is [4, 45, 6] with sum 55 (> 51).
```

**Example 2:**

```text
Input: x = 100, arr = [1, 10, 5, 2, 7]
Output: 0
Explanation:
No subarray has a sum strictly greater than 100.
```

## Explanation & Intuition

1. **Variable-Size Sliding Window:**
   Since all elements in `arr` are positive, adding elements increases the subarray sum and removing elements from the left decreases it. This monotonic property allows us to use a two-pointer sliding window (`left` and `right`).

2. **Expand & Contract Strategy:**
   * **Expand (`right` pointer):** Iterate `right` from $0$ to $N - 1$, adding `arr[right]` to `current`.
   * **Contract (`left` pointer):** As soon as `current > x`, we have a valid candidate subarray `[left..right]` of length `right - left + 1`. We update `min_len` and greedily shrink the window from the left (`current -= arr[left]`, `left += 1`) to see if an even shorter subarray still satisfies `current > x`.

3. **Fallback Check:**
   `min_len` is initialized to `length + 1` (an impossible subarray length). If no valid subarray was ever found, `min_len` remains `length + 1`, and we return `0`.

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$

  Both the `right` and `left` pointers traverse the array at most once, meaning each element is added and removed at most one time ($2N$ operations in the worst case).

* **Space Complexity:** $\mathcal{O}(1)$

  Only a few integer variables (`length`, `current`, `min_len`, `left`) are used regardless of input size.

## Implementation & Unit Testing

Below is the complete Python 3 implementation along with a `unittest` suite covering standard cases, single-element matches, exact-sum boundary cases, and cases where no valid subarray exists:

```python
import unittest


class Solution:
    def smallestSubWithSum(self, arr: list[int], x: int) -> int:
        length = len(arr)
        current = 0
        # Initialize min_len to an unreachable value greater than array length
        min_len = length + 1
        left = 0

        # Expand the sliding window by moving the right pointer
        for right in range(length):
            current += arr[right]

            # Shrink the window from the left while the sum remains strictly greater than x
            while current > x:
                min_len = min(min_len, right - left + 1)
                current -= arr[left]
                left += 1

        # Return min_len if a valid subarray was found; otherwise, return 0
        return min_len if min_len <= length else 0


class TestSmallestSubWithSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard_cases(self):
        # [4, 45, 6] -> sum 55 > 51, length 3
        self.assertEqual(self.sol.smallestSubWithSum([1, 4, 45, 6, 0, 19], 51), 3)
        # [4, 45, 6, 10, 19] -> length 2 ([45, 6] = 51 > 50)
        self.assertEqual(self.sol.smallestSubWithSum([1, 4, 45, 6, 10, 19], 50), 2)

    def test_single_element_exceeds_x(self):
        # [8] alone is strictly greater than 7
        self.assertEqual(self.sol.smallestSubWithSum([1, 2, 8, 3], 7), 1)

    def test_no_valid_subarray(self):
        # Total sum is 25, which is not > 100
        self.assertEqual(self.sol.smallestSubWithSum([1, 10, 5, 2, 7], 100), 0)

    def test_strictly_greater_boundary(self):
        # Entire array sums to 10, which is NOT strictly greater than 10
        self.assertEqual(self.sol.smallestSubWithSum([2, 3, 5], 10), 0)
        # Entire array sums to 10, which IS strictly greater than 9
        self.assertEqual(self.sol.smallestSubWithSum([2, 3, 5], 9), 3)


if __name__ == "__main__":
    unittest.main()
```