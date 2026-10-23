# User function Template for python3

'''
# BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root) -> int:
        # Step 1: Perform inorder traversal to extract elements
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Count inversions using Merge Sort approach
        def merge_and_count(left_arr, right_arr):
            i = j = count = 0
            merged = []
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    merged.append(left_arr[i])
                    i += 1
                else:
                    # If left_arr[i] > right_arr[j], then all remaining elements 
                    # in left_arr from index i to the end form an inversion pair.
                    merged.append(right_arr[j])
                    count += (len(left_arr) - i)
                    j += 1
                    
            merged.extend(left_arr[i:])
            merged.extend(right_arr[j:])
            return merged, count

        def merge_sort_and_count(sub_arr):
            if len(sub_arr) <= 1:
                return sub_arr, 0
                
            mid = len(sub_arr) // 2
            left_sorted, left_count = merge_sort_and_count(sub_arr[:mid])
            right_sorted, right_count = merge_sort_and_count(sub_arr[mid:])
            merged, split_count = merge_and_count(left_sorted, right_sorted)
            
            return merged, left_count + right_count + split_count

        _, total_inversions = merge_sort_and_count(arr)
        return total_inversions
