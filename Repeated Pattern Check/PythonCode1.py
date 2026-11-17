class Solution:
    def findPattern(self, s):
        i, l = 0, len(s)
        while i < l:
            x, y = 0, 0
            while i < l and s[i] == 'x':
                x += 1
                i += 1
            while i < l and s[i] == 'y':
                y += 1
                i += 1
            if x != y:
                return False
        return True
