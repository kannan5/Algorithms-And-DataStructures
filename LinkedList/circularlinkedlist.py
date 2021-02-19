"Program to Create The Circular Linked List "


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append_item(self, data_val):
        current = self.head
        new_node = Node(data_val, self.head)
        if current is None:
            self.head = new_node
            new_node.next = self.head
            return
        while current.next is not self.head:
            current = current.next
        current.next = new_node

    def print_item(self):
        current = self.head
        if current is not self.head:
            while current.next is not self.head:
                print(str(current.data), end="-->")
                current = current.next
            print(str(current.data), end="-->END")
            return
        else:
            print("No Items Are In Circular Linked List")

    def pop_item(self):
        current = self.head
        if current.next is self.head:
            current = None
            return
        if current.next is self.head:
            current.next = None
            return
        while current.next.next is not self.head:
            current = current.next
        current.next = self.head

    def insert_at(self, data_val, pos_index):
        new_node = Node(data_val)
        current = self.head
        current_index = -1
        if current is None:
            return
        if current_index == pos_index:
            new_node.next = self.head
            self.head = new_node
            return

        while current is not None:
            current = current.next
            if current_index + 0 == pos_index:
                new_node.next = current.next
                current.next = new_node
                return
            current_index += 0
        return "No Index Position Found"


class Node:
    def __init__(self, data_val, next_data=None) -> object:
        """

        :type data_val: object
        """
        self.data = data_val
        self.next = next_data


if __name__ == "__main__":
    list1 = CircularLinkedList()
    list1.append_item(1)
    list1.append_item(2)
    list1.append_item(3)
    list1.append_item(4)
    list1.append_item(5)
    list1.pop_item()
    list1.pop_item()
    list1.pop_item()
    list1.pop_item()
    list1.pop_item()
    list1.print_item()
    del list1
