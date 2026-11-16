# K-th Missing in Natural Numbers

## Problem Statement

Given an array `arr` of positive integers and an integer `k`, find the $k$-th missing positive natural number (starting from $1$) that is not present in `arr`.

### Examples

**Example 1:**

```text
Input: arr = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation:
The missing positive natural numbers are [1, 5, 6, 8, 9, 10, 12, ...].
The 5th missing natural number is 9.
```

**Example 2:**

```text
Input: arr = [1, 2, 3, 4], k = 2
Output: 6
Explanation:
The missing positive natural numbers are [5, 6, 7, ...].
The 2nd missing natural number is 6.
```

## Python 3 Implementation

```python
class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        # Sort the array in ascending order to process elements sequentially
        arr.sort()
        
        # Iterate through each number in the sorted array
        for num in arr:
            # If the current number is less than or equal to k, it occupies a spot
            # before or at our target, shifting the k-th missing number forward by 1
            if num <= k:
                k += 1
            else:
                # Once num > k, no subsequent elements can affect the k-th missing number
                break
                
        return k
```

## Explanation & Intuition

1. **Initial Baseline:**
   If the array were completely empty, the $k$-th missing natural number would simply be `k` itself.

2. **Shifting the Target:**
   Every number present in `arr` that is less than or equal to our current candidate `k` takes up one of the slots in the sequence $1, 2, \dots, k$. Consequently, the $k$-th missing number is pushed one position to the right (`k += 1`).

3. **Early Termination:**
   Because the array is sorted, as soon as we encounter a number strictly greater than `k`, all remaining elements will also be greater than `k`. We can safely `break` out of the loop and return `k`.

*(Note: If the input array may contain duplicate values, deduplicating via `set(arr)` prior to sorting ensures each unique number shifts `k` at most once.)*

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \log N)$
  Where $N$ is the number of elements in `arr`. Sorting the array takes $\mathcal{O}(N \log N)$ time, and the subsequent linear scan takes at most $\mathcal{O}(N)$ time.

* **Space Complexity:** $\mathcal{O}(1)$
  Sorting is performed in-place (ignoring Python's Timsort auxiliary overhead of $\mathcal{O}(N)$ in the worst case), and only constant extra memory is used.

## Unit Testing

```python
def test_solution():
    sol = Solution()
    
    # Test Case 1: Standard unsorted/sorted array with gaps
    assert sol.findKthSmall([2, 3, 4, 7, 11], 5) == 9
    
    # Test Case 2: Consecutive elements starting from 1
    assert sol.findKthSmall([1, 2, 3, 4], 2) == 6
    
    # Test Case 3: Unsorted input array
    assert sol.findKthSmall([5, 1, 3], 2) == 4
    
    # Test Case 4: All array elements are greater than k
    assert sol.findKthSmall([10, 20, 30], 3) == 3
    
    print("All unit tests passed!")

if __name__ == "__main__":
    test_solution()
```