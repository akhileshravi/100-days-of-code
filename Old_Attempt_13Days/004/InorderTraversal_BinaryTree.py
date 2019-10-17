# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        prev_list = []
        node = A
        trav = []
        while True:
            if node is None:
                if prev_list:
                    node = prev_list[-1]
                    del prev_list[-1]
                    node.left = None
                else:
                    break
            if node.left is None:
                trav.append(node.val)
                if node.right is not None:
                    node = node.right
                elif prev_list:
                    node = prev_list[-1]
                    del prev_list[-1]
                else:
                    break
            else:
                prev_list.append(node)
                node = node.left
        return trav
                