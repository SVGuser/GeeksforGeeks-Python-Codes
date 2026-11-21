class Solution:
    def smallestSubWithSum(self, arr, x):
        length = len(arr)
        current = 0
        min_len = length + 1
        left = 0
        for right in range(length):
            current += arr[right]
            while current > x:
                min_len = min(min_len, right - left + 1)
                current -= arr[left]
                left += 1
        return min_len if min_len <= length else 0
