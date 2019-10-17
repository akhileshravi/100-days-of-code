# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def numbers(self, A, l = ['']):
        if A is None:
            return l
        
        if A.left is None and A.right is None:
            l1 = [i + str(A.val) for i in l]
            return l1
        
        left, right = [], []
        if A.left is not None:
            left = self.numbers(A.left, l)
        if A.right is not None:
            right = self.numbers(A.right, l)
        
        return left + right
        
    def sumNumbers(self, A):
        numlist = self.numbers(A)
        # if A.left is not None:
        #     numlist = self.numbers(A.left)
        # return A.left is None
        return numlist #sum([int(i) % 1003 for i in numlist])
        
        