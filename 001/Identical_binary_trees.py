# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        
        if A is None and B is None:
            return 1
            
        if not (A is not None and B is not None):
            return 0
        
        if A.val != B.val:
            return 0
        
        leftcond = Solution.isSameTree(self, A.left, B.left)
        rightcond = Solution.isSameTree(self, A.right, B.right)
        
        return int(leftcond and rightcond)
