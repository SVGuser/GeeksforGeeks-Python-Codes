# Check Path in Graph (BFS)

## Code
```python
from collections import deque

class Solution:

    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:

        if u == v:
            return True

        vis = set([u])
        queue = deque([u])

        while queue:
            current = queue.popleft()

            for child in adj[current]:
                if child == v:
                    return True

                if child not in vis:
                    vis.add(child)
                    queue.append(child)

        return False
```

## Steps Involved

1. Import `deque` from `collections` for efficient queue operations.
2. Define the `checkPath()` method that checks whether a path exists from node `u` to node `v`.
3. If `u` and `v` are the same node, return `True` immediately.
4. Create a visited set `vis` and mark `u` as visited.
5. Initialize a queue with the starting node `u`.
6. Perform Breadth-First Search (BFS) while the queue is not empty.
7. Remove the front node from the queue and store it in `current`.
8. Traverse all adjacent nodes (`child`) of `current`.
9. If any adjacent node equals `v`, a path exists, so return `True`.
10. If an adjacent node has not been visited, mark it visited and push it into the queue.
11. Continue until all reachable nodes are explored.
12. If node `v` is never found, return `False`.

## Time Complexity

- **O(V + E)**

## Space Complexity

- **O(V)**

## Approach

This solution uses **Breadth-First Search (BFS)** to explore the graph level by level starting from node `u`. If node `v` is encountered during traversal, the function immediately returns `True`. Otherwise, after visiting all reachable nodes, it returns `False`.
