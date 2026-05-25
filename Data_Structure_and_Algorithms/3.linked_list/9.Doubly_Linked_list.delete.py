class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def output_node_reverse(head):
    # find tail
    i = head
    while i.next is not None:
        i = i.next;

    while i is not None:
        print(i.data, end=' '); i = i.prev

def output_node_directly(head):
    i = head
    while i is not None:
        print(i.data, end=' '); i = i.next

def delete_node_head(head):
    i = head
    head = i.next
    return head

def delete_specific_location(head, location):
    i = head
    for j in range(0, location-2, 1):
        i = i.next
    prev_node = i.prev; next_node = i.next
    prev_node.next = next_node; next_node.prev = prev_node #this line still not working
    return head

node1 = Node(10)
node2 = Node(20); node1.next = node2; node2.prev = node1
node3 = Node(30); node2.next = node3; node3.prev = node2

output_node_reverse(node1); print()
output_node_directly(node1); print()

head = delete_node_head(node1)
output_node_directly(head); print()

head = delete_specific_location(node1, 2)
output_node_directly(head); print()