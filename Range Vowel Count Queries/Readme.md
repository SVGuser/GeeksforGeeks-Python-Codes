# Count Vowels in Range Queries

## Problem
Given a string `s` and a list of queries `queries`, where each query consists of two indices `[l, r]`, return the number of vowels present in the substring `s[l:r+1]` for every query.

## Approach
Use a **Prefix Sum** array to store the cumulative count of vowels up to each index.

- Create a set of vowels for O(1) lookup.
- Build a prefix array where:
  - `prefix[i]` represents the number of vowels in the first `i` characters.
- For a query `[l, r]`, the vowel count is:
  
  ```python
  prefix[r + 1] - prefix[l]
  ```

## Complexity Analysis

- **Building Prefix Array:** `O(n)`
- **Each Query:** `O(1)`
- **Total:** `O(n + q)`

where:
- `n` = length of the string
- `q` = number of queries

## Python Solution

```python
class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = set("aeiouAEIOU")

        n = len(s)
        prefix = [0] * (n + 1)

        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if ch in vowels else 0)

        return [prefix[r + 1] - prefix[l] for l, r in queries]
```

## Example

### Input

```python
s = "abecid"
queries = [[0, 2], [1, 4], [2, 5]]
```

### Output

```python
[2, 2, 2]
```

### Explanation

| Query | Substring | Vowel Count |
|---------|-----------|-------------|
| [0, 2] | "abe" | 2 |
| [1, 4] | "beci" | 2 |
| [2, 5] | "ecid" | 2 |

## Key Idea

Prefix sums allow us to answer each range query in constant time after a single preprocessing pass through the string.
