# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def depthbal(self, A):
        if A is None:
            return 0, True
        flag = True
        if A.left is not None:
            left = Solution.depthbal(self, A.left)
            if not left[2]:
                flag = False
            elif abs(left[1]-left[0]) > 1:
                flag = False
            left = 1 + max([left[0], left[1]])
        else:
            left = 0
            
        if A.right is not None:
            right = Solution.depthbal(self, A.right)
            if not right[2]:
                flag = False
            elif abs(right[1]-right[0]) > 1:
                flag = False
            right = 1 + max([right[0], right[1]])
        else:
            right = 0
        
        if abs(left - right) > 1:
            flag = False
        return left, right, flag
        
    def isBalanced(self, A):
        t = (Solution.depthbal(self, A))
        if abs(t[0] - t[1]) > 1:
            return 0
        if not t[-1]:
            return 0
        
        return 1
            
        
