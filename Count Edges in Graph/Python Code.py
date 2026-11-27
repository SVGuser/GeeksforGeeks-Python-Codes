class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        total = sum(len(childs) for childs in adj)
        return total // 2
