import sys
input = sys.stdin.readline

class binary_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = binary_tree(value)
        return self.left

    def insert_right(self, value):
        self.right = binary_tree(value)
        return self.right

def insert_node(node, value):
    global total
    if value < node.value:
        if node.left == None:
            node.insert_left(value)
        else:
            insert_node(node.left, value)
    else:
        if node.right == None:
            node.insert_right(value)
        else:
            insert_node(node.right, value)

N = int(input())
tree = binary_tree(int(input()))

for i in range(N-1):
    value = int(input())
    insert_node(node, value)
