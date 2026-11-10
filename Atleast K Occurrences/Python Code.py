class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        group = {}
        for num in arr:
            group[num] = group.get(num, 0) + 1
            if group[num] == k :
                return num
        return -1
