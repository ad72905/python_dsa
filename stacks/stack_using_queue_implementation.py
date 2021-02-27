# Stack implementation using queue:
# We are given a queue which is an abstract data type and has a FIFO behaviour
# We are internally assuming that the queue is having it's implementation using an array

from queue import Queue

class Stack:

    def __init__(self):
        self.queue = []

    def check_empty(self):
        return self.queue == []



