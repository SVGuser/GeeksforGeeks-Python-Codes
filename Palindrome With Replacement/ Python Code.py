class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        s_list = list(s)
        
        # Step 1: Enforce palindromic matching from ends to center
        for i in range(n // 2):
            left = i
            right = n - 1 - i
            
            if s_list[left] != '?' and s_list[right] != '?':
                if s_list[left] != s_list[right]:
                    return -1
            elif s_list[left] != '?':
                s_list[right] = s_list[left]
            elif s_list[right] != '?':
                s_list[left] = s_list[right]
                
        # Handle the absolute middle character if n is odd
        # (It doesn't affect palindromic symmetry, but we should fill it if it's '?')
        
        # Step 2: Fill remaining '?' to minimize adjacent differences
        # We propagate known characters to neighboring '?' positions
        
        # Left-to-right propagation
        last_char = None
        for i in range(n):
            if s_list[i] != '?':
                last_char = s_list[i]
            elif last_char is not None:
                s_list[i] = last_char
                
        # Right-to-left propagation (for any leading '?' that didn't get filled)
        last_char = None
        for i in range(n - 1, -1, -1):
            if s_list[i] != '?':
                last_char = s_list[i]
            elif last_char is not None:
                s_list[i] = last_char
                
        # If the string was entirely '?', fill it with 'a'
        for i in range(n):
            if s_list[i] == '?':
                s_list[i] = 'a'
                
        # Re-enforce palindrome symmetry just in case propagation caused mismatch 
        # (e.g. middle independent choices)
        for i in range(n // 2):
            s_list[n - 1 - i] = s_list[i]
            
        # Step 3: Calculate the minimum absolute ASCII sum of adjacent pairs
        total_sum = 0
        for i in range(n - 1):
            total_sum += abs(ord(s_list[i]) - ord(s_list[i+1]))
            
        return total_sum
