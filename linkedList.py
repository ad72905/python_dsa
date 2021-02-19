# Linked List Implementation:
# ---------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):

        # because we are adding data, let's increment the size
        self.size = self.size + 1
        # creating a fresh node
        new_node = Node(data)

        # checking if it's an empty list or not
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):

        # because we are adding data, let's increment the size
        self.size = self.size + 1
        # creating a fresh node
        new_node = Node(data)
        # assigning a node iterator
        current_node = self.head

        # traversing the list till the end
        while current_node.next_node is not None:
            current_node = current_node.next_node

        # inserting the new item
        current_node.next_node = new_node

    def size_of_list(self):
        print('Size of the Linked List currently is :', self.size)
        return self.size

    def traverse(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(5)
    linked_list.insert_start(10)
    linked_list.insert_end(12)
    linked_list.size_of_list()
    linked_list.traverse()
