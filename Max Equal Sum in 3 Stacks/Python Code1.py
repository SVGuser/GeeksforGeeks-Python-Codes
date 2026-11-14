class Solution:
  def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
    add1, add2, add3 = sum(s1), sum(s2), sum(s3)
    L, E, G = 0, 0, 0
    G1, G2, G3 = len(s1), len(s2), len(s3)
    while L < G1 and E < G2 and G < G3:
      if add1 == add2 == add3:
        return add1
      if add1 >= add2 and add1 >= add3:
        add1 -= s1[L]
        L += 1
      elif add2 >= add1 and add2 >= add3:
        add2 -= s2[E]
        E += 1
      else:
        add3 -= s3[G]
        G += 1
    return 0
