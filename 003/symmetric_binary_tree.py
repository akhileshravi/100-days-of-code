# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def flip_id(self, A, B):
        if A is None and B is None:
            return True
        c = 0
        c += int(A is None)
        c += int(B is None)
        if c == 1:
            return 0
        
        if A.val != B.val:
            return False
        
        cond1 = self.flip_id(A.left, B.right)
        cond2 = self.flip_id(A.right, B.left)
        
        return (cond1 and cond2)
    
    def isSymmetric(self, A):
        if A is None:
            return 1
            
        return int( self.flip_id(A.left, A.right) )
        
 
