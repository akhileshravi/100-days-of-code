class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.ins = 'L'

def Heap:
    def __init__(self):
        self.root = None

    def insert(self, val, node = self.root, prev = self.root):
        
        if node is None:
            if prev == node: # root
               self.root = Node(val)
            else:
                if prev.state == 'L':
                    prev.left = Node(val)
                    node = prev.left
                elif prev.state == 'R':
                    prev.right = Node(val)
                    node = prev.right

                if node.val < prev.val:
                    node.val, prev.val = prev.val, node.val

        else:
            if node.ins == 'L':
                self.insert(val, node.left, node)
                node.ins = 'R'
            elif node.ins == 'R':
                self.insert(val, node.right, node)
                node.ins = 'L'
            if node != prev:# not root
                if node.val < prev.val:
                    node.val, prev.val = prev.val, node.val
                

    def delete_min(self):
        if self.root is None:
            return
        elif self.root.left is None and self.right is None:
            val = self.root.val
            self.root = None
            return val
        val = self.root.val
        node = self.root
        prev = self.root
        state = None
        while True:
            if node.left is None and node.right is None:
                if state == 'right':
                    prev.right = None
                elif state == 'left':
                    prev.left = None
                break
            elif node.left is None:
                node.val = node.right.val
                prev = node
                node = node.right
                state = 'right'
            elif node.right is None:
                node.val = node.left.val
                prev = node
                node = node.left
                state = 'left'
            else:
                if node.left.val <= node.right.val:
                    node.val = node.left.val
                    prev = node
                    node = node.left
                    state = 'left'
                else:
                    node.val = node.right.val
                    prev = node
                    node = node.right
                    state = 'right
        return val
