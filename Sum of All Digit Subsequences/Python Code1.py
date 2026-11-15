class Solution:
    def subsequenceSum(self, s: str) -> int:
        # Define modulo constant as required by the problem
        MOD = 10 ** 9 + 7
        
        # Store the length of the digit string
        add = len(s)
        
        # Calculate the sum of all individual digits in the string
        letter = sum(int(g) for g in s)
        
        # Each digit appears in exactly 2^(n - 1) subsequences
        # Multiply total digit sum by 2^(n - 1) under modulo
        res = (letter * pow(2, add - 1, MOD)) % MOD
        
        return res
