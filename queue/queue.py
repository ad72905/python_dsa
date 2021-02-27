# Queue implementation using an array

class Queue:

    def __init__(self):
        self.queue = []

    def check_empty(self):
        return self.queue == []

    def queue_size(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.check_empty():
            print('Oops! Queue is empty')
            return
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

    def view(self):
        print('Currently, the queue is as below\n', self.queue)


if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(12)
    queue.enqueue(52)
    queue.enqueue(25)
    queue.enqueue(35)
    queue.enqueue(76)
    queue.enqueue(24)
    queue.enqueue(43)

    print('Queue size:', queue.queue_size())
    queue.view()

    print('Dequeue begins:')
    print(queue.dequeue())
    print('Queue size:', queue.queue_size())
    print(queue.dequeue())
    print('Queue size:', queue.queue_size())
    print(queue.dequeue())
    print('Queue size:', queue.queue_size())
    print(queue.dequeue())

    queue.view()

