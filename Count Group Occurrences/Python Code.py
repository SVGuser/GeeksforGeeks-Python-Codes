class Solution:
  def getCount(self, s, k):
    if not s:
      return 0
    group = {}
    group[s[0]] = 1
    for n in range(1, len(s)):
      if s[n] != s[n - 1]:
        group[s[n]] = group.get(s[n], 0) + 1
    word = 0
    for m in group.values():
      if m == k:
        word += 1
    return word
