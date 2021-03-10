"""

    This Program will Implements Queue Structure and It's Operation Using Stacks

"""


class Queue:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def enqueue(self, new_val):
        if len(self.S1) > 0:
            self.S2 = self.S1[:]
            self.S1.clear()
        self.S1.append(new_val)
        if len(self.S2) > 0:
            self.S1.extend(self.S2)
        self.S2.clear()

    def dequeue(self):
        if len(self.S1) <= 0:
            return
        x = self.S1[-1]
        self.S1.pop(-1)
        return x

    def peek_value(self):
        for x in self.S1:
            print(x)

if __name__ == "__main__":
    c = Queue()
    c.enqueue(1)
    c.enqueue(2)
    c.peek_value()