"""Create Linked List Classes"""


class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, data_val):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = data_val

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_by_index(self, search_index):
        current_index = 0
        current = self.head
        if current_index == search_index:
            self.head = current.next
        while current is not None:
            if current_index + 1 == search_index:
                if current.next.next is not None:
                    current.next = current.next.next
                else:
                    current.next = None
            current = current.next
            current_index += 1

    def delete_by_value(self, data_val):
        current = self.head
        if current.data == data_val:
            self.head = current.next
        while current is not None:
            if current.next.next is not None:
                if data_val == current.next.data:
                    current.next = current.next.next
            else:
                if data_val == current.next.data:
                    current.next = None
            current = current.next

    def search_by_value(self, search_value):
        current = self.head
        current_index = 0
        while current is not None:
            if search_value == current.data:
                return str(search_value) + " Is In Index Of " + str(current_index)
            current_index += 1
            current = current.next
        return "Not Found"

    def reverse_list(self):
        if self.head is None:
            return None

    def reverse_recursive(self, current=None, prev=None):
        if current is None and prev is None:
            current = self.head
            next_el = None
        if current.next is None and prev is not None:
            self.head = current
            current.next = prev
            return
        next_el = current.next
        current.next = prev
        prev = current

        self.reverse_recursive(next_el, prev)

    def detect_loops_hash(self):
        current = self.head
        hash_map = set()
        while current is not None:
            if current in hash_map:
                return True
            set.add(current)
        return False

    def detect_loops_floyd(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Node:
    def __init__(self, data_val):
        self.data = data_val
        self.next = None


if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.add_item(Node(4))
    list1.add_item(Node(5))
    list1.reverse_recursive()
    list1.print_list()
    del list1
