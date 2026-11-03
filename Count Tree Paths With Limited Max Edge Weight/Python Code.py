class Solution:
    def maximumWeight(self, n, edges, queries):
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        sorted_edges = sorted(edges, key=lambda x: x[2])
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                new_paths = size[root_i] * size[root_j]
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                return new_paths
            return 0
        ans = [0] * len(queries)
        current_paths = 0
        edge_idx = 0
        num_edges = len(sorted_edges)
        for q_idx, x in sorted_queries:
            while edge_idx < num_edges and sorted_edges[edge_idx][2] <= x:
                u, v, w = sorted_edges[edge_idx]
                current_paths += union(u, v)
                edge_idx += 1
            ans[q_idx] = current_paths
        return ans
