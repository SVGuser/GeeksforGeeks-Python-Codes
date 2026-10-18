class Solution:
  def minimumStep(self, n):
    min_edge = 0
    while n > 1:
      if n % 3 == 0:
        n //= 3
      else:
        n -= 1
      min_edge += 1
    return min_edge
