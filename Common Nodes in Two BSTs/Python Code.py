class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        p1, p2 = [], []
        ans = []
        
        while True:
            # Push all left nodes of first BST
            if r1:
                p1.append(r1)
                r1 = r1.left
            # Push all left nodes of second BST
            elif r2:
                p2.append(r2)
                r2 = r2.left
            # Both r1 and r2 are None, compare tops of both stacks
            elif p1 and p2:
                r1 = p1[-1]
                r2 = p2[-1]
                
                if r1.data == r2.data:
                    ans.append(r1.data)
                    p1.pop()
                    p2.pop()
                    # Move to inorder successors
                    r1 = r1.right
                    r2 = r2.right
                elif r1.data < r2.data:
                    p1.pop()
                    r1 = r1.right
                    r2 = None  # Reset r2 so we don't re-push its left subtree
                else:
                    p2.pop()
                    r2 = r2.right
                    r1 = None  # Reset r1 so we don't re-push its left subtree
            else:
                break
                
        return res
