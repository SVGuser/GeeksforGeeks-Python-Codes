class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        n = len(s)

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                freq[char_idx] += 1

                max_f = 0
                min_f = float('inf')

                for h in freq:
                    if h > 0:
                        if h > max_f:
                            max_f = h
                        if h < min_f:
                            min_f = h

                total += (max_f - min_f)

        return total
