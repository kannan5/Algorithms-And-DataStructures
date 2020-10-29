# Binary Search Tree
class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, new_item):
        self.items.insert(0, new_item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        return self.items[-1].data

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].data

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def level_order_traversal(start, ord_type):
    if start is None:
        return
    new_queue = Queue()
    new_queue.enqueue(start)
    traversal = ""

    if ord_type == "backward":
        stack = Stack()

    while len(new_queue) > 0:
        if ord_type == "forward":
            traversal += str(new_queue.peek()) + "-"
            node = new_queue.dequeue()
            if node.left:  # If Node Have Left child
                new_queue.enqueue(node.left)
            if node.right:  # If Node Have a right child
                new_queue.enqueue(node.right)
        if ord_type == "backward":
            node = new_queue.dequeue()
            stack.push(node)
            if node.right:  # If Node Have a right child
                new_queue.enqueue(node.right)
            if node.left:  # If Node Have Left child
                new_queue.enqueue(node.left)

    if ord_type == "backward":
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.data) + "-"
    return traversal


class BST:
    def __init__(self, val=None):
        self.root = Node(val)

    def insert(self, cur_node, data):
        if cur_node is None:
            return
        cur_data = cur_node.data
        if cur_data == data:
            print("the Value is Already Exit")
            return
        if data < cur_data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.insert(cur_node.left, data)

        elif data > cur_data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.insert(cur_node.right, data)

    def find(self, node, val):
        cur_node = node.data
        if cur_node == val:
            return "Value Exist In The Tree"
        if cur_node > val and node.left:
            return self.find(node.left, val)
        if cur_node < val and node.right:
            return self.find(node.right, val)
        else:
            return "Value Not Exist in The Tree"

    def pre_order_traversal(self, node, traversal):
        if node:
            traversal += (str(node.data) + "-")
            traversal = self.pre_order_traversal(node.left, traversal)
            traversal = self.pre_order_traversal(node.right, traversal)
        return traversal

    def in_order_traversal(self, node, traversal):
        if node:
            traversal = self.pre_order_traversal(node.left, traversal)
            traversal += (str(node.data) + "-")
            traversal = self.pre_order_traversal(node.right, traversal)
        return traversal

    def post_order_traversal(self, node, traversal):
        if node:
            traversal = self.pre_order_traversal(node.left, traversal)
            traversal = self.pre_order_traversal(node.right, traversal)
            traversal += (str(node.data) + "-")
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type.lower() == "preorder":
            print(self.pre_order_traversal(self.root, "") + "END")
        elif traversal_type.lower() == "inorder":
            print(self.in_order_traversal(self.root, "") + "END")
        elif traversal_type.lower() == "level_order":
            print(level_order_traversal(self.root, "forward") + "END")
        elif traversal_type.lower() == "reverse_level_order":
            print(level_order_traversal(self.root, "backward") + "END")
        else:
            print("The Traversal Type " + traversal_type + " Is Not Supported")


if __name__ == "__main__":
    a = BST(15)
    a.root.left = Node(10)
    a.root.right = Node(25)
    a.root.left.left = Node(5)
    a.root.left.right = Node(12)
    a.root.right.left = Node(20)
    a.root.right.right = Node(35)
    a.insert(a.root, 40)
    a.insert(a.root, 8)
    print(a.find(a.root, 10))
    print(a.pre_order_traversal(a.root, ""))
