
# Stack is an abstract data type and is used to implement Last-In-First-Out (LIFO) behavior
# Stack implementation using array data structure

class Stack:

    def __init__(self):
        self.stack = []

    def empty_check(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.empty_check():
            print('Oops! Stack is empty!')
            return
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

    def view(self):
        print('Currently, the stack is as below\n', self.stack)


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


