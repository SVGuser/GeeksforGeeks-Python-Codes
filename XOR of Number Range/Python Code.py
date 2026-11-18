class Solution:
    def findXOR(self, l: int, r: int) -> int:
        # Helper function to compute the XOR of all numbers from 0 to n
        def totalXOR(n: int) -> int:
            # Base case for negative bounds (e.g., when l = 0, l - 1 = -1)
            if n < 0:
                return 0
            
            # The cumulative XOR from 0 to n follows a strict cycle of length 4
            rem = n % 4
            if rem == 0:
                return n
            elif rem == 1:
                return 1
            elif rem == 2:
                return n + 1
            else:
                return 0
