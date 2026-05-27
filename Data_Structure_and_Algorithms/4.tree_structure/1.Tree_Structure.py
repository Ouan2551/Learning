# Node structure for Tree
class Node:
    def __init__(self, x):
        self.data = x
        self.children = []

# Add children to a node
def add_children(parent, child):
    parent.children.append(child)

# Print parent of each node
def print_parent(node, parent):
    if parent is None:
        

# main part
root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# constructing tree
add_children(root, n2)
add_children(root, n3)
add_children(n2, n4)
add_children(n3, n5)

print("Parent of each node:")
print_parent(root, None)