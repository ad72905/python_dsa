# Stack implementation using a linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def empty_check(self):
        return self.head is None

    def stack_size(self):
        return self.size

    def push(self, data):
        self.size = self.size + 1
        if self.empty_check():
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next_node = self.head
            self.head = node

    def pop(self):
        if self.empty_check():
            print('Oops! Stack is empty')
            return
        elif self.size == 1:
            data = self.head.data
            del self.head
            self.size = self.size - 1
            return data
        else:
            data = self.head.data
            head = self.head
            self.head = self.head.next_node
            del head
            self.size = self.size - 1
            return data

    def view(self):
        if self.empty_check():
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, end=' ')
                node = node.next_node


if __name__ == '__main__':
    stack = Stack()

    stack.push(12)
    stack.push(52)
    stack.push(25)
    stack.push(35)
    stack.push(76)
    stack.push(24)
    stack.push(43)
    print('Stack size:', stack.stack_size())
    stack.view()

    print('Pop begins:')
    print(stack.pop())
    print('Stack size:', stack.stack_size())
    print(stack.pop())
    print('Stack size:', stack.stack_size())
    print(stack.pop())
    print('Stack size:', stack.stack_size())
    print(stack.pop())
    print('Stack size:', stack.stack_size())

    stack.view()

