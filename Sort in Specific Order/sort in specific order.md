# Sort in Specific Order (Odd Descending, Even Ascending)

This repository contains a clean Python implementation for sorting an array of integers such that all **odd numbers** appear first in **descending order**, followed by all **even numbers** in **ascending order**.

---

## 📋 Problem Statement

Given an array `arr` of integers, rearrange the elements in-place according to the following rules:
1. All **odd** numbers must be placed at the beginning of the array, sorted in **descending** order.
2. All **even** numbers must be placed after the odd numbers, sorted in **ascending** order.

### Example

**Input:**
```text
arr = [1, 2, 3, 5, 4, 7, 10]
```

**Output:**
```text
[7, 5, 3, 1, 2, 4, 10]
```

**Explanation:**
* Odd elements: `[1, 3, 5, 7]` $\rightarrow$ Sorted descending: `[7, 5, 3, 1]`
* Even elements: `[2, 4, 10]` $\rightarrow$ Sorted ascending: `[2, 4, 10]`
* Combined result: `[7, 5, 3, 1, 2, 4, 10]`

---

## 💡 Approach

1. **Partitioning:** Use list comprehensions to separate the elements of `arr` into two distinct lists: `odd` and `even`.
2. **Sorting:** 
   - Sort the `odd` list in descending order (`reverse=True`).
   - Sort the `even` list in ascending order.
3. **In-Place Update:** Concatenate the two lists and overwrite the original array using slice assignment (`arr[:] = odd + even`) so the reference is preserved.

---

## ⏱️ Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \log N)$  
  Where $N$ is the number of elements in `arr`. Partitioning takes $\mathcal{O}(N)$ time, and sorting the two sublists takes $\mathcal{O}(N \log N)$ in the worst case.
* **Space Complexity:** $\mathcal{O}(N)$  
  Auxiliary space is used to store the temporary `odd` and `even` lists.

---

## 🚀 Usage

Clone the repository and run the Python script directly:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python solution.py
```

### Importing into your project

```python
from solution import Solution

sol = Solution()
data = [0, 4, 5, 3, 7, 2, 1]
sol.sortIt(data)
print(data)  # Output: [7, 5, 3, 1, 0, 2, 4]
```