class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        square = 0
        noSquare = 0
        ans = 0

        for curr in arr:
            newNosquare = max(curr, noSquare + curr)
            newSquare = max(curr * curr, max(noSquare + curr * curr, square + curr))
            noSquare = newNosquare
            square = newSquare
            ans = max(ans, max(noSquare, square))

        return ans
