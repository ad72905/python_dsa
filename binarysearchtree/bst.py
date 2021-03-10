
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild is None:
                node.leftChild = Node(data, node)
            else:
                self.insert_node(data, node.leftChild)
        else:
            if node.rightChild is None:
                node.rightChild = Node(data, node)
            else:
                self.insert_node(data, node.rightChild)

    def traverse(self):
        if self.root is None:
            return
        else:
            self.traverse_subtree(self.root.leftChild)
            print(self.root.data)
            self.traverse_subtree(self.root.rightChild)

    def traverse_subtree(self, node):
        if node is None:
            return
        else:
            self.traverse_subtree(node.leftChild)
            print(node.data)
            self.traverse_subtree(node.rightChild)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(12)
    bst.insert(8)
    bst.insert(10)
    bst.insert(14)
    bst.insert(5)
    bst.insert(11)
    bst.insert(3)
    bst.insert(-8)
    bst.insert(75)
    bst.insert(13)

    bst.traverse()