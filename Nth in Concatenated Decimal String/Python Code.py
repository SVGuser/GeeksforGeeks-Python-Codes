class Solution:
    def nthCharacter(self, n):
        nums = 1
        cnt = 9
        start = 1
        while n > nums * cnt:
            n -= nums * cnt
            nums += 1
            cnt *= 10
            start *= 10
        actual_num = start + (n - 1) // nums
        digit = (n - 1) % nums
        return int(str(actual_num)[digit])
