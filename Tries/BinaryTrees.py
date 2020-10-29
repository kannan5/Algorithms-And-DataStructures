# Binary Tree Creation and It's Operations.

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


class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val=None):
        self.root = Node(val)

    def print_tree(self, traversal_type):
        if traversal_type.lower() == "preorder":
            print(self.pre_order_traversal(self.root, "") + "END")
        elif traversal_type.lower() == "inorder":
            print(self.in_order_traversal(self.root, "") + "END")
        elif traversal_type.lower() == "level_order":
            print(self.level_order_traversal(self.root, "forward") + "END")
        elif traversal_type.lower() == "reverse_level_order":
            print(self.level_order_traversal(self.root, "backward") + "END")
        else:
            print("The Traversal Type " + traversal_type + " Is Not Supported")

    def pre_order_traversal(self, start, traversal):
        # Pre-Order Traversal
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def in_order_traversal(self, start, traversal):
        # In-Order Traversal
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def level_order_traversal(self, start, type):
        if start is None:
            return
        new_queue = Queue()
        new_queue.enqueue(start)
        traversal = ""

        if type == "backward":
            stack = Stack()

        while len(new_queue) > 0:
            if type == "forward":
                traversal += str(new_queue.peek()) + "-"
                node = new_queue.dequeue()
                if node.left:  # If Node Have Left child
                    new_queue.enqueue(node.left)
                if node.right:  # If Node Have a right child
                    new_queue.enqueue(node.right)
            if type == "backward":
                node = new_queue.dequeue()
                stack.push(node)
                if node.right:  # If Node Have a right child
                    new_queue.enqueue(node.right)
                if node.left:  # If Node Have Left child
                    new_queue.enqueue(node.left)

        if type == "backward":
            while len(stack) > 0:
                node = stack.pop()
                traversal += str(node.data) + "-"
        return traversal

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_tree(self):
        stack = Stack()    # Iterative way of Find Size Of Tree
        stack.push(self.root)
        tree_size = 1
        while stack:
            node = stack.pop()
            if node.left:
                tree_size += 1
                stack.push(node.left)
            if node.right:
                tree_size += 1
                stack.push(node.right)
        return tree_size

    def rec_size_tree(self, node):
        if node is None:    # Recursive Find Size Of Tree
            return 0
        return 1 + self.rec_size_tree(node.left) + self.rec_size_tree(node.right)


if __name__ == "__main__":
    a = Tree(10)
    a.root.left = Node(5)
    a.root.left.left = Node(3)
    a.root.left.right = Node(6)
    a.root.right = Node(15)
    a.root.right.left = Node(20)
    a.root.right.right = Node(25)
    a.root.right.right.right = Node(35)
    a.print_tree("inorder")
    a.print_tree("preorder")
    a.print_tree("level_order")
    a.print_tree("reverse_level_order")
    print(a.height(a.root))
    print(a.size_tree())
    print(a.rec_size_tree(a.root))
