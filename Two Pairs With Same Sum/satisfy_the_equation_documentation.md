# `findPairs` — Satisfy the Equation ($A + B = C + D$)

**Problem Link:** [Satisfy the Equation — GeeksforGeeks](https://www.geeksforgeeks.org/problems/satisfy-the-equation5847/1)

## Overview

Given an array `arr` of $n$ integers, the `findPairs` method finds four **distinct** indices $(A, B, C, D)$ such that:

$$
\text{arr}[A] + \text{arr}[B] = \text{arr}[C] + \text{arr}[D]
$$

If multiple valid quadruples exist, the method returns the **lexicographically smallest** quadruple $[A, B, C, D]$. If no valid quadruple exists, it returns `[-1, -1, -1, -1]`.

## Key Insight

* Iterating over all pairs $(i, j)$ with $0 \le i < j < n$ in ascending order guarantees that the **first time** any sum $S = \text{arr}[i] + \text{arr}[j]$ is encountered, it is produced by the lexicographically earliest pair $(x, y)$ for that sum.
* Therefore, we only need to store the **first** occurrence `(x, y)` of each pair sum in a hash map (`first`). Any subsequent pair `(i, j)` with the same sum only needs to be checked against that earliest pair `(x, y)`—provided all four indices $x, y, i, j$ are distinct.
* Because `(i, j)` is visited in increasing order, multiple valid quadruples can still arise across *different* sums (for example, sum $S_1$ discovered later might have a smaller starting index $x$ than sum $S_2$). Tracking `No_duplicate` with standard list comparison (`needed_arr < No_duplicate`) ensures the globally lexicographically smallest valid quadruple is returned.

## Implementation

```python
class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        first = {}
        No_duplicate = None
        for i in range(n):
            for j in range(i + 1, n):
                current = arr[i] + arr[j]
                if current not in first:
                    first[current] = (i, j)
                else:
                    x, y = first[current]
                    if x != i and x != j and y != i and y != j:
                        needed_arr = [x, y, i, j]
                        if No_duplicate is None or needed_arr < No_duplicate:
                            No_duplicate = needed_arr
        return No_duplicate if No_duplicate is not None else [-1, -1, -1, -1]
```

## Step-by-Step Breakdown

1. **Initialize Tracking Structures:**
   * `first`: A dictionary mapping a pair sum `current` $\to$ `(x, y)`, storing only the earliest index pair with that sum.
   * `No_duplicate`: Stores the best (lexicographically smallest) valid quadruple `[x, y, i, j]` found so far, initialized to `None`.
2. **Enumerate All Index Pairs $(i, j)$ with $i < j$:**
   * Compute `current = arr[i] + arr[j]`.
   * **Unseen Sum:** Store `first[current] = (i, j)`.
   * **Existing Sum:** Retrieve the earliest pair `x, y = first[current]`.
3. **Validate Distinct Indices & Update Best Quadruple:**
   * Verify `x != i and x != j and y != i and y != j` so no array element is reused.
   * Construct `needed_arr = [x, y, i, j]` (note that since `first[current]` was recorded earlier, $(x, y) < (i, j)$ automatically).
   * Update `No_duplicate` if it is `None` or if `needed_arr < No_duplicate`.
4. **Return Result:**
   * Return `No_duplicate` if a valid quadruple was found; otherwise return `[-1, -1, -1, -1]`.

## Example Walkthrough

Suppose `arr = [3, 4, 7, 1, 2, 9, 8]`:

| Pair `(i, j)` | Values `(arr[i], arr[j])` | `current` Sum | Action / State Update |
| :--- | :--- | :--- | :--- |
| `(0, 1)` | `(3, 4)` | $7$ | Store `first[7] = (0, 1)` |
| `(0, 2)` | `(3, 7)` | $10$ | Store `first[10] = (0, 2)` |
| `(0, 3)` | `(3, 1)` | $4$ | Store `first[4] = (0, 3)` |
| `(0, 4)` | `(3, 2)` | $5$ | Store `first[5] = (0, 4)` |
| `(0, 5)` | `(3, 9)` | $12$ | Store `first[12] = (0, 5)` |
| `(0, 6)` | `(3, 8)` | $11$ | Store `first[11] = (0, 6)` |
| `(1, 2)` | `(4, 7)` | $11$ | Match `first[11] = (0, 6)`; all indices `{0, 6, 1, 2}` distinct $\implies$ `No_duplicate = [0, 6, 1, 2]` |
| `(1, 3)` | `(4, 1)` | $5$ | Match `first[5] = (0, 4)`; all indices `{0, 4, 1, 3}` distinct and `[0, 4, 1, 3] < [0, 6, 1, 2]` $\implies$ `No_duplicate = [0, 4, 1, 3]` |
| `(1, 4)` | `(4, 2)` | $6$ | Store `first[6] = (1, 4)` |
| `(1, 5)` | `(4, 9)` | $13$ | Store `first[13] = (1, 5)` |
| `(1, 6)` | `(4, 8)` | $12$ | Match `first[12] = (0, 5)`; `[0, 5, 1, 6] > [0, 4, 1, 3]`, keep `[0, 4, 1, 3]` |
| `(2, 3)` | `(7, 1)` | $8$ | Store `first[8] = (2, 3)` |
| `(2, 4)` | `(7, 2)` | $9$ | Store `first[9] = (2, 4)` |
| `(3, 4)` | `(1, 2)` | $3$ | Store `first[3] = (3, 4)` |
| `(3, 5)` | `(1, 9)` | $10$ | Match `first[10] = (0, 2)`; `[0, 2, 3, 5] < [0, 4, 1, 3]` $\implies$ `No_duplicate = [0, 2, 3, 5]` |
| $\dots$ | $\dots$ | $\dots$ | Remaining pairs produce no lexicographically smaller quadruple |

**Final Output:** `[0, 2, 3, 5]` (since $\text{arr}[0] + \text{arr}[2] = 3 + 7 = 10$ and $\text{arr}[3] + \text{arr}[5] = 1 + 9 = 10$).

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n^2)$ — There are $\frac{n(n - 1)}{2}$ pairs $(i, j)$, and each hash map lookup, insertion, and 4-element list comparison runs in $\mathcal{O}(1)$ average time.
* **Space Complexity:** $\mathcal{O}(n^2)$ — In the worst case (when all pair sums are distinct), `first` stores up to $\frac{n(n - 1)}{2}$ entries.