class Solution:
  def countBT(self, h: int) -> int:
    MOD = 10 ** 9 + 7
    # Base Cases
    if h == 0 or h == 1:
      return 1
    count = 0
    next_count = 0
    for k in range(2, h + 1):
      # T(h) = T(h-1) * ((T(h-1) + 2 * T(h - 2))
      curr = (next_count * (next_count + 2 * count)) % MOD
      count = next_count
      next_count = curr
    return next_count
