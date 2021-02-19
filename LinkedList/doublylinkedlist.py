
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append_item(self, data_val):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node(data_val, current)

    def add_by_index(self, data_val, index):
        current = self.head
        current_index = 0
        while current is not None:
            if index < current_index:
                return IndexError("Invalid Index")
            if index == current_index + 1:
                if current.next is not None:
                    new_node = node(data_val, current, current.next)
                else:
                    new_node = node(data_val, current)
                temp = current.next
                temp.prev = new_node
                current.next = new_node
                return
            current = current.next
            current_index += 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(str(current.data), end=" --> ")
            current = current.next
        print("END")

    def pop_list(self):
        current = self.head
        if current is None:
            return
        if current.next is None:
            self.head = None
            return
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_by_index(self, index):
        current = self.head
        current_index = 0
        if current is None:
            return
        if index == 0:
            self.head = current.next
        while current is not None:
            if current_index + 1 == index:
                rem_node = current.next
                current.next = rem_node.next
                return
            current_index += 1
            current = current.next


class node:
    def __init__(self, data_val, prev_data=None, next_data=None):
        self.prev = prev_data
        self.data = data_val
        self.next = next_data


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    newNode = node(1)
    newSecondNode = node(2, newNode)
    newNode.next = newSecondNode
    newSecondNode.next = node(4, newSecondNode)
    list1.head = newNode
    list1.append_item(5)
    list1.add_by_index(3, 2)
    list1.print_list()

