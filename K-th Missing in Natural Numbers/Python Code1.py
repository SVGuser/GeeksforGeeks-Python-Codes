class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        # Sort the array in ascending order to process elements sequentially
        arr.sort()
        
        # Iterate through each number in the sorted array
        for num in arr:
            # If the current number is less than or equal to k, it occupies a spot
            # before or at our target, shifting the k-th missing number forward by 1
            if num <= k:
                k += 1
            else:
                # Once num > k, no subsequent elements can affect the k-th missing number
                break
                
        return k
