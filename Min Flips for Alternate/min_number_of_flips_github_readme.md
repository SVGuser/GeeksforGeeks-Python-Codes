# Min Number of Flips

- **Platform:** GeeksforGeeks
- **Difficulty:** Easy
- **Problem Link:** [Min Number of Flips](https://www.geeksforgeeks.org/problems/min-number-of-flips3210/1)

---

## 📝 Problem Statement

Given a binary string `s`, that is, a string containing only `'0'`s and `'1'`s. We need to make this string a sequence of alternate characters by flipping some of the bits. Our goal is to minimize the number of bits to be flipped.

### Examples

**Example 1:**
```text
Input: s = "001"
Output: 1
Explanation: 
We can flip the 0th bit to '1' to have "101".
```

**Example 2:**
```text
Input: s = "0001010111"
Output: 2
Explanation: 
We can flip the 1st and 8th bit to have "0101010101".
```

---

## 💡 Intuition & Approach

For any binary string of length $N$ to have alternating characters, there are only **two possible valid target patterns**:
1. Starting with `'0'`: `"010101..."`
2. Starting with `'1'`: `"101010..."`

We can simulate creating both alternating strings using a helper function `numberofflips(start)`:
- Initialize a tracker `helpflip` with the starting character (`'0'` or `'1'`).
- Iterate through each character in the input string `s`.
- If the current character doesn't match `helpflip`, increment the `flips` counter.
- Toggle `helpflip` between `'0'` and `'1'` for the next position.
- Finally, return the minimum flips required between the two patterns.

---

## 💻 Solution (Python)

```python
class Solution:
    def minFlips(self, s):
        def numberofflips(start: str) -> int:
            helpflip = start
            flips = 0
            for i in s:
                if i != helpflip:
                    flips += 1
                helpflip = '1' if helpflip == '0' else '0'
            return flips
            
        return min(numberofflips('0'), numberofflips('1'))
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of the string `s`. We traverse the string twice (once for each starting pattern).
- **Space Complexity:** $O(1)$, as we only use a few variables to keep track of the expected bit and flip counts.