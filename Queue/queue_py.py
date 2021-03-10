"""
Implement the Queue Data Structure Using Python

Note: In This Class Queue was implemented using Python Lists.
        List is Not Suitable or Won't be efficient for Queue Structure.
            (Since It Takes O(n) for Insertion and Deletion).
                This is for Understanding / Learning Purpose.

"""


class Queue:
    def __init__(self):
        self.queue = list()

    def add_element(self, data_val):
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def pop_element(self, value):
        self.queue.remove(value)


if __name__ == "__main__":
    q = Queue()
    q.add_element(1)
    q.add_element(2)
    q.add_element(2)
    for x, y in vars(q).items():
        print(x, y)
