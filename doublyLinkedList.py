# Doubly Linked List Implementation:
# ----------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)

        # if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.size == 1:
            # insert at the end if list has only one element
            self.head.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        else:
            # insert at the end if list has more than one element
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

        self.size = self.size + 1

    def size_of_list(self):
        print('Size of Linked List :', self.size)
        return self.size

    def traverse(self):

        # assigning a node pointer
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insert(10)
    linked_list.insert(13)
    linked_list.insert(15)
    linked_list.insert(35)
    linked_list.size_of_list()
    linked_list.traverse()
