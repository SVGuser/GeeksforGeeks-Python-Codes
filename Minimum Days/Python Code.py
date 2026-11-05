class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        c = len(s)
        string = list(s)
        collide = 0
        for r in range(c - 1):
            if string[r] == string[r + 1]:
                collide += 1
        if collide == 0:
            return 0
        for one in range(c):
            index = p[one]
            if index > 0 and string[index] == string[index - 1]:
                collide -= 1
            if index < c - 1 and string[index] == string[index + 1]:
                collide -= 1
            string[index] = '?'
            if collide == 0:
                return one + 1
        return 0
