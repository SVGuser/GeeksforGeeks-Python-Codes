class Solution:
  def posInfinite(self, s: str, pos: int) -> str:
    length = len(s)
    step = 1
    while length < pos:
      length = 2 * length + step
      step += 1
    while step > 1:
      step -= 1
      previous_length = (length - step) // 2
      if previous_length < pos <= previous_length + step:
        return '$'
      elif pos > previous_length + step:
        pos = length - pos + 1
      length = previous_length
    return s[pos - 1]
