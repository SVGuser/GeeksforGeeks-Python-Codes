from collections import deque
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        if u == v:
            return True
        vis = set([u])
        queue  = deque([u])
        while queue:
            current = queue.popleft()
            for child in adj[current]:
                if child == v:
                    return True
                if child not in vis:
                    vis.add(child)
                    queue.append(child)
        return False
