arr1 = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K"]


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class snode:
    def __int__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Trees:
    def __init__(self, data=None):
        self.root = data

    def df_traversal(self, node_list):
        if node_list is None:
            return
        print(node_list.data)
        if node_list.left:
            self.df_traversal(node_list.left)
        if node_list.right:
            self.df_traversal(node_list.right)


if __name__ == '__main__':
    a = Trees()
    node_list = Node("A",Node("B",Node("E"),Node("F", Node("I"), Node("J"))),Node("D",Node("G", Node("K")),Node("H")))
    # node_list = Node("A", )
    a.df_traversal(node_list)
