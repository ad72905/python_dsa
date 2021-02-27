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

    # O(1)
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

    # O(N)
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

    # O(1)
    def size_of_list(self):
        print('Size of the Linked List currently is :', self.size)
        return self.size

    # O(N)
    def traverse(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    # O(N)
    def remove(self, data):

        # case of empty list
        if self.head is None:
            print('The list is empty')
            return
        # assigning node iterators for current node and previous node
        current_node = self.head
        previous_node = None

        # Possible cases of removal : Removal from beginning, in between and end
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if current_node is None:
            print('Item not present in the list')
            return

        # Checking if it is a header entry to be removed or a different entry
        # In case of header we can also use condition of previous_node == null also
        if current_node.data == data and current_node == self.head:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

        del current_node
        self.size = self.size - 1
        print('Updated Linked List post removal is as :')
        self.traverse()
        self.size_of_list()
        return self


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(5)
    linked_list.insert_start(10)
    linked_list.insert_end(12)
    linked_list.size_of_list()
    linked_list.traverse()
    linked_list.remove(10)
