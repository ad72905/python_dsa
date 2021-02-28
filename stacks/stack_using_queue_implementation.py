# Stack implementation using queue:
# We are given instances of queue which is an abstract data type and has a FIFO behaviour
# We are internally assuming that the queue is having it's implementation using an array

from queue import Queue


class Stack:

    # initialisation
    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    # returns the stack size at any point
    def stack_size(self):
        return self.queue_1.queue_size()

    # making an expensive push operation
    def push(self, data):

        self.queue_2.enqueue(data)
        while self.queue_1.queue_size() != 0:
            self.queue_2.enqueue(self.queue_1.dequeue())

        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

    # O(1) pop operation
    def pop(self):
        if self.queue_1.queue_size() == 0:
            print('Oops! Stack is empty')
            return
        else:
            return self.queue_1.dequeue()

    def view(self):
        print('Currently the stack is as below\n')
        self.queue_1.view()


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
