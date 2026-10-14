class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        diff = [0] * (n + 1)
        for k in roll:
            diff[0] += 1
            if k < n:
                diff[k] -= 1
        res = []
        curr = 0
        for i in range(n):
            curr += diff[i]
            original = ord(s[i]) - ord('a')
            pos = (original + curr) % 26
            res.append(chr(pos + ord('a')))
        return "".join(res)

# Whole Program given below to test 
def findRollOut(s, roll):
    n = len(s)
    s_list = list(s)  # Convert string to list because strings are immutable in Python
    
    # Process each roll operation
    for r in roll:
        # Determine how many characters to roll (cannot exceed string length)
        limit = min(r, n)
        
        # Roll the characters in the current prefix
        for i in range(limit):
            if s_list[i] == 'z':
                s_list[i] = 'a'  # Wrap around from 'z' to 'a'
            else:
                s_list[i] = chr(ord(s_list[i]) + 1)  # Increment character
                
    return "".join(s_list)

# Example usage:
s = "bca"
roll = [1, 2, 3]
print(findRollOut(s, roll))  # Output: eeb
