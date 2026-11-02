class Solution:
    def largestSumCycle(self, edge):
        a = len(edge)
        vis = [False] * a
        cycles = -1
        for i in range(a):
            if not vis[i]:
                curr = i
                path = []
                curr_path = {}
                while curr != -1 and not vis[curr]:
                    if curr in curr_path:
                        start_idx = curr_path[curr]
                        sum_cycle = sum(path[start_idx:])
                        cycles = max(cycles, sum_cycle)
                        break
                    
                    curr_path[curr] = len(path)
                    path.append(curr)
                    curr = edge[curr]
                for node in path:
                    vis[node] = True
        return cycles
