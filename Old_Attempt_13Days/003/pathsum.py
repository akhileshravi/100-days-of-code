# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if A is None:
            return int(B == 0)
        # if A.val > B:
            # return False
        #  if A.val == B and (A.left is not None or A.right )
        
        if A.left is None and A.right is None:
            return int(A.val == B)
        
        if A.left is not None:
            if Solution.hasPathSum(self, A.left, B - A.val):
                return 1
        if A.right is not None:
            if Solution.hasPathSum(self, A.right, B - A.val):
                return 1
        
        return 0
 
