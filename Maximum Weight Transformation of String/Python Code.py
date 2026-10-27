class Solution:
    def getMaxWeight(self, s):
        if not s:
            return 0
        cost_X = 0 if s[0] == 'A' else 1
        cost_Y = 1 if s[0] == 'A' else 0
        dp = [1 - cost_X, 1 - cost_Y, float('-inf'), float('-inf')]
        for i in range(1, len(s)):
            cost_X = 0 if s[i] == 'A' else 1
            cost_Y = 1 if s[i] == 'A' else 0
            prev_max = max(dp)
            nxt_dp = [
                prev_max + 1 - cost_X,
                prev_max + 1 - cost_Y,
                dp[1] + 3 - cost_X,
                dp[0] + 3 - cost_Y
            ]
            dp = nxt_dp
        return max(dp)
