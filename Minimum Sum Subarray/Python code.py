class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        n = len(arr)
        minimum = arr[0]
        curr = arr[0]
        for i in range(1, n):
            curr = min(arr[i], curr + arr[i])
            minimum = min(minimum, curr)
        return minimum
