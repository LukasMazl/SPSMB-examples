class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            node = self.root
            while True:
                if key < node.value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(key)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(key)
                        break
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

bt = BinaryTree()

tree = [1, 3, 10, 5, 2, 100]

for i in tree:
    bt.insert(i)

bt.inorder(bt.root)
