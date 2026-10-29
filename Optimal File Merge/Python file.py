import heapq
class Solution:
    def minComputation(self, files):
      # Turn thw files list into a min heap in-place
        heapq.heapify(files)
        total = 0
      # Keep merging until only one files remains
        while len(files) > 1:
          # Extract the two smallest file sizes
            one = heapq.heappop(files)
            two = heapq.heappop(files)
          # Thw cost to mereg them
            curr = one + two
            total += curr
          # Push the combined file back into thr min - heap
            heapq.heappush(files, curr)
        return total
