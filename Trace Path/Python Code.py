class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        p, q = 0, 0
        min_x, max_x = 0, 0
        min_y, max_y = 0, 0
        for cell in s:
            if cell == 'L':
                q -= 1
            elif cell == 'R':
                q += 1
            elif cell == 'U':
                p -= 1
            elif cell == 'D':
                p += 1
            min_x = min(min_x, p)
            max_x = max(max_x, p)
            min_y = min(min_y, q)
            max_y = max(max_y, q)
        required_height = max_x -min_x + 1
        required_width = max_y - min_y + 1
        return required_height <= n and required_width <= m
