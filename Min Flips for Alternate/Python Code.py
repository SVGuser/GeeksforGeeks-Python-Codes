class Solution:
    def minFlips(self, s):
        def numberofflips(start: str) -> int:
            helpflip = start
            flips = 0
            for i in s:
                if i != helpflip:
                    flips += 1
                helpflip = '1' if helpflip == '0' else '0'
            return flips
        return min(numberofflips('0'), numberofflips('1'))
