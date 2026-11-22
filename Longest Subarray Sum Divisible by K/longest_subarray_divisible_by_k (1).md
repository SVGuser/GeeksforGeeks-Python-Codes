# Longest Subarray with Sum Divisible by K

## Problem Statement
Given an array of integers `arr` and a positive integer `k`, find the length of the longest contiguous subarray whose sum is divisible by `k`.

---

## Intuition & Approach
To solve this problem efficiently without checking all possible subarrays ($O(N^2)$), we can use **Prefix Sums** combined with a **Hash Map** (dictionary).

### Key Mathematical Property
Let $P_i$ be the prefix sum from index $0$ to $i$, and $P_j$ be the prefix sum from index $0$ to $j$ (where $j < i$). 
The sum of the subarray from index $j+1$ to $i$ is:
$$\text{Subarray Sum} = P_i - P_j$$

For this subarray sum to be divisible by $k$:
$$(P_i - P_j) \pmod k = 0 \implies P_i \pmod k = P_j \pmod k$$

This means that if two prefix sums leave the **same remainder** when divided by $k$, the elements strictly between those two indices form a subarray whose sum is divisible by $k$.

### Algorithm Steps
1. **Initialize a Hash Map:** Store `{0: -1}` in `hash_map` to handle cases where a prefix sum starting from index `0` is directly divisible by `k`.
2. **Track Running Sum & Max Length:** Initialize `pref = 0` (running prefix sum) and `large = 0` (maximum subarray length found so far).
3. **Iterate Through the Array:**
   - Add the current element `num` to `pref`.
   - Compute `condition = pref % k`. *(Note: In Python, `% k` always yields a non-negative remainder in the range $[0, k-1]$ when $k > 0$, cleanly handling negative numbers in `arr`.)*
   - **If `condition` exists in `hash_map`:** Calculate the subarray length `current = i - hash_map[condition]` and update `large = max(large, current)`. We **do not** overwrite the index in `hash_map` because we want the earliest occurrence to maximize the subarray length.
   - **If `condition` is not in `hash_map`:** Record the first occurrence of this remainder: `hash_map[condition] = i`.
4. **Return Result:** Return `large` after the loop finishes.

---

## Code Implementation

```python
class Solution:
    def longestSubarrayDivK(self, arr, k):
        # Maps remainder -> first index where this remainder occurred
        hash_map = {0: -1}
        pref, large = 0, 0
        
        for i, num in enumerate(arr):
            pref += num
            condition = pref % k
            
            if condition in hash_map:
                current = i - hash_map[condition]
                large = max(large, current)
            else:
                hash_map[condition] = i
                
        return large
```

---

## Dry Run Example
**Input:** `arr = [2, 7, 6, 1, 4, 5]`, `k = 3`

| Index (`i`) | `num` | `pref` | `pref % 3` | `hash_map` State | `current` Length | `large` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *Init* | - | `0` | - | `{0: -1}` | - | `0` |
| `0` | `2` | `2` | `2` | `{0: -1, 2: 0}` | - | `0` |
| `1` | `7` | `9` | `0` | `{0: -1, 2: 0}` | `1 - (-1) = 2` | `2` |
| `2` | `6` | `15` | `0` | `{0: -1, 2: 0}` | `2 - (-1) = 3` | `3` |
| `3` | `1` | `16` | `1` | `{0: -1, 2: 0, 1: 3}` | - | `3` |
| `4` | `4` | `20` | `2` | `{0: -1, 2: 0, 1: 3}` | `4 - 0 = 4` | `4` |
| `5` | `5` | `25` | `1` | `{0: -1, 2: 0, 1: 3}` | `5 - 3 = 2` | `4` |

**Output:** `4` (corresponding to subarray `[7, 6, 1, 4]`, sum = `18`, which is divisible by `3`).

---

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of `arr`. We traverse the array once, and hash map lookups/insertions take $\mathcal{O}(1)$ average time.
* **Space Complexity:** $\mathcal{O}(\min(N, k))$, since there are at most $k$ possible remainders ($0$ to $k-1$) stored in the hash map, bounded by the $N$ elements in the array.