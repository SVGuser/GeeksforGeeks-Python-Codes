class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        join_node = float('inf')
        current = root
        while current:
            join_node = min(join_node, abs(current.data - k))
            if current.data == k:
                return 0
            elif k < current.data:
                current = current.left
            else:
                current = current.right
        return join_node
