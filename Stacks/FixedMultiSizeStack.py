import numpy as np


class FixedMultiStack:
    NumberOfStack = 3
    StackCapacity = 0
    values = None
    sizes = None

    def __init__(self, stack_size):
        self.values = np.empty(stack_size * self.NumberOfStack)
        self.sizes = np.empty(stack_size)
        self.StackCapacity = stack_size

    def stack_push(self, stack_no, value):
        if self.is_fullstack(stack_no):
            Exception("Stack Is Full")
        self.values[self.sizes[stack_no] + stack_no] = value
        self.sizes[stack_no] += 1

    def pop(self, stack_no):
        if self.is_empty_stack(stack_no):
            Exception("There Is No Element to Delete In Stack")
        val = self.values[self.index_top_of(stack_no)]
        self.values[self.index_top_of(stack_no)] = None
        self.sizes[stack_no] -= 1
        return val

    def index_top_of(self, stack_no):
        start = (stack_no - 1) * self.StackCapacity
        size = self.sizes[stack_no]
        return start + size

    def is_empty_stack(self, stack_no):
        return self.sizes[stack_no] == self.StackCapacity

    def is_fullstack(self, stack_no):
        return self.sizes[stack_no] == self.StackCapacity


if __name__ == '__main__':
    a = FixedMultiStack(4)

    a.stack_push(1,1)
    a.stack_push(1,2)
    a.stack_push(2,1)
    a.stack_push(2,2)
    a.stack_push(2,3)
    a.stack_push(3,1)
    a.stack_push(3,2)
    a.pop(1)