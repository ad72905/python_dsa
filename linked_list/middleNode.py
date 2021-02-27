# Defining a single node in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# Defining a Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # generally, we insert a node at the beginning of the node since it is an O(1)
    def insert(self, data):

        new_node = Node(data)

        # empty list check
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        # increment the size
        self.size = self.size + 1

        return self.head

    # check for current status of list size
    def size_of_list(self):
        return self.size

    # traverse and print the final list
    def traverse(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def mid_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        if self.size % 2 == 0:
            print('The middle observations are :', slow_pointer.data, slow_pointer.next_node.data)
            return slow_pointer.data, slow_pointer.next_node.data
        else:
            print('The middle observation is :', slow_pointer.data)
        return slow_pointer.data


# function to find the middle node in a linked list
def middle_node(input_list):

    if input_list.size_of_list() == 0:
        print('Sorry, the list is empty')
    elif input_list.size_of_list == 1:
        print('The middle node of the list is :', input_list.head.data)
    else:
        count = 0
        current_node = input_list.head
        previous_node = None
        while count < input_list.size_of_list()//2:
            previous_node = current_node
            current_node = current_node.next_node
            count = count + 1

        if input_list.size_of_list()%2 == 0:
            print('The middle nodes of the list are :', previous_node.data, current_node.data)
            return previous_node.data, current_node.data
        else:
            print('The middle node of the list is :', current_node.data)
            return current_node.data


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(12)
    linked_list.insert(98)
    linked_list.insert(21)
    linked_list.insert(56)
    linked_list.insert(85)
    linked_list.traverse()
    print('Size of Linked List :', linked_list.size_of_list())
    middle_node(linked_list)
    linked_list.mid_node()
