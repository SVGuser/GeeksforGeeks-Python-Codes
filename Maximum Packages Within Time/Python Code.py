class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        if totalTime <= 0 or n == 0:
            return 0
        if totalTime >= n:
            return sum(arr)
        initial = sum(arr[:totalTime])
        max_pack = initial
        for i in range(totalTime, n):
            initial += arr[i] - arr[i - totalTime]
            max_pack = max(max_pack, initial)
        return max_pack
