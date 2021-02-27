# define node
class Node:

    # initialize node with given data and point next node to null
    def __init__(self,data):
        self.data = data
        self.next_node = None


class LinkedList:

    # initialize list with null head and 0 size
    def __init__(self):
        self.head = None
        self.size = 0

    # returns the list at any given point in time
    def size_of_list(self):
        return self.size

    # always insertion at the beginning in case of list since O(1)
    def insert(self, data):
        new_node = Node(data)

        if self.size == 0:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.size = self.size + 1

    # traverse the entire list and print it's contents
    def traverse(self):
        current_node = self.head
        if self.size == 0:
            print('Oops, the list is empty!')
        else:
            print('The linked list created is as below :')
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next_node

    # reverse a given linked list (using an in-place algorithm)
    def reverse(self):
        # nothing to be reversed if the list is empty
        if self.size == 0:
            return
        if self.size == 1:
            return self.head.data

        else:
            previous_node = None
            next_node = None
            current_node = self.head
            while current_node:
                next_node = current_node.next_node
                current_node.next_node = previous_node
                previous_node = current_node
                current_node = next_node
            self.head = previous_node
        return self


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert(12)
    linked_list.insert(25)
    linked_list.insert(65)
    linked_list.insert(29)
    linked_list.insert(75)
    linked_list.insert(64)
    linked_list.insert(42)
    linked_list.insert(59)
    linked_list.insert(20)
    linked_list.traverse()
    print('\nThe size of the linked list is :', linked_list.size_of_list())
    linked_list.reverse().traverse()




