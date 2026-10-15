"""
Problem: Maximum Without 3 Consecutive Set Bits (GeeksforGeeks)
Link: https://www.geeksforgeeks.org/problems/geek-hates-too-many-1s--170647/1
"""

class Solution:
    def maxValue(self, n: int) -> int:
        """
        Calculates the maximum possible value from n such that no 
        three consecutive bits are set (1).
        
        :param n: Non-negative integer
        :return: Modified integer meeting the constraints
        """
        res = n
        
        # Iterate from the 30th bit down to 2
        for i in range(30, 1, -1):
            # Check if the i-th, (i-1)-th, and (i-2)-th bits are all set
            if (res & (1 << i)) and (res & (1 << (i - 1))) and (res & (1 << (i - 2))):
                # Clear the lowest bit of the three consecutive set bits
                res &= ~(1 << (i - 2))
                
        return res

# Driver code to test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1} -> Output: {sol.maxValue(n1)}")  # Expected: 2
    
    # Test case 2
    n2 = 7
    print(f"Input: n = {n2} -> Output: {sol.maxValue(n2)}")  # Expected: 6
    
    # Test case 3
    n3 = 15
    print(f"Input: n = {n3} -> Output: {sol.maxValue(n3)}")  # Expected: 13 (1111 -> 1101)
