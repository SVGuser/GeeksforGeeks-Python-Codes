class Solution:
  def checkWithinK(self, arr: list[int], k : int)-> bool:
    update = set()
    for i, num in enumerate(arr):
      if num in update:
        return True
      update.add(num)
      if len(update) > k:
        update.remove(arr[i - k])
    return False
