# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def exist(self, A, B, C, final=None):
        if A is None:
            return False, False, None
        left = self.exist(A.left, B, C, final)
        right = self.exist(A.right, B, C, final)
        
        if left[2] is not None:
            return True, True, left[2]
        if right[2] is not None:
            return True, True, right[2]
        
        now = [False, False]
        
        if left[0] or right[0] or A.val == B:
            now[0] = True
        
        if left[1] or right[1] or A.val == C:
            now[1] = True
        
        if now[0] and now[1]:
            final = A.val
        
        return now[0], now[1], final
        
    def lca(self, A, B, C):
        now = self.exist(A, B, C)
        if now[2] is not None:
            return now[2]
        else:
            return -1
