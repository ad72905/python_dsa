# Queue implementation using two stacks with pop only operation
# Enable enqueue, dequeue

class Queue:

    def __init__(self):

        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):

        self.enqueue_stack.append(data)

    def dequeue(self):

        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            print('Error as stacks are empty')
            return

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

            return self.dequeue_stack.pop()

        else:
            return self.dequeue_stack.pop()


if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(12)
    queue.enqueue(20)
    queue.enqueue(85)
    queue.enqueue(75)
    print('Queue : ', queue.enqueue_stack, end=' ')
    print('\n')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())