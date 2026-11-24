class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        first = {}
        No_duplicate = None
        for i in range(n):
            for j in range(i + 1, n):
                current = arr[i] + arr[j]
                if current not in first:
                    first[current] = (i, j)
                else:
                    x, y = first[current]
                    if x != i and x != j and y != i and y != j:
                        needed_arr = [x, y, i, j]
                        if No_duplicate is None or needed_arr < No_duplicate:
                            No_duplicate = needed_arr
        return No_duplicate if No_duplicate is not None else [-1, -1, -1, -1]
