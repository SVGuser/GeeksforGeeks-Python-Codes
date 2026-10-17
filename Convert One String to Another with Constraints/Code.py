class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        seq1 = [(char, i) for i, char in enumerate(s1) if char != '#']
        seq2 = [(char, j) for j, char in enumerate(s2) if char != '#']
        if len(seq1) != len(seq2):
            return False
        for (char1, i), (char2, j) in zip(seq1, seq2):
            if char1 != char2:
                return False
            if char1 == 'A' and i < j:
                return False
            if char1 == 'B' and i > j:
                return False
        return True
