from typing import List

class Solution:
    def sortIt(self, arr: List[int]) -> List[int]:
        """
        Sorts all odd numbers in descending order and all even numbers
        in ascending order in-place.

        Args:
            arr (List[int]): Input list of integers.

        Returns:
            List[int]: The modified list with sorted odd and even elements.
        """
        odd = [x for x in arr if x % 2 != 0]
        even = [x for x in arr if x % 2 == 0]
        
        odd.sort(reverse=True)
        even.sort()
        
        arr[:] = odd + even
        return arr


if __name__ == "__main__":
    # Example Usage
    solver = Solution()
    sample_arr = [1, 2, 3, 5, 4, 7, 10]
    print("Original Array:", sample_arr)
    solver.sortIt(sample_arr)
    print("Sorted Array:  ", sample_arr)
