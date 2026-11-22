class Solution:
  def longestSubarrayDivK(self, arr, k):
    hash_map = {-1: 0}
    pref, large = 0, 0
    for i, num in enumerate(arr):
      pref += num
      condition = pref % k
      if condition in hash_map:
        current = i - hash_map[condition]
        large = max(large, current)
      else:
        hash_map[condition] = i
    return large
