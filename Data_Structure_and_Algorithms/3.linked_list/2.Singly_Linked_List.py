# create base for node
class Node:
    def __init__(self, data1):
        # "__init__" ensures node has a 'data' and 'next_pointer'
        self.data = data1 
        self.next = None
        # linked list in 1 node has 3 sections | previous | data | next |
        # 'self' stand for control each node

node1 = Node(15)
node2 = Node(3)
node3 = Node(67)

node1.next = node2
node2.next = node3

head = node1
current = head