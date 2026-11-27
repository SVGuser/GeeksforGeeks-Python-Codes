# Count Edges in Graph | GeeksforGeeks

## Solution

```python
class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        total = sum(len(childs) for childs in adj)
        return total // 2
```

## Approach

In an undirected graph, every edge appears twice in the adjacency list:

- Once from `u` to `v`
- Once from `v` to `u`

So if we sum the sizes of all adjacency lists, every edge is counted twice.

Formula:

Number of Edges = (Sum of Adjacency List Sizes) / 2

## Complexity

- Time Complexity: **O(V + E)**
- Space Complexity: **O(1)**
