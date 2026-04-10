class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def output_linked_list_forward(head):
    i = head
    while i is not None:
        print(i.data, end=' ')
        i = i.next

def insert_at_begin(head, x):
    i = head
    data = Node(x)
    data.next = i
    head = data
    return head

def insert_at_tail(head, x):
    i = head
    data = Node(x)
    while i.next is not None:
        i = i.next
    i.next = data
    return head

def insert_at_custom_location(head, x, location):
    i = head; data = Node(x); count = int(0)
    for j in range(0, location-2, 1):
        i = i.next
    next_node = i.next
    i.next = data
    data.prev = i
    data.next = next_node
    if next_node is not None:
        next_node.prev = data
    return head

data1 = Node(10)
data2 = Node(20); data1.next = data2; data2.prev = data1
data3 = Node(30); data2.next = data3; data3.prev = data2
head = data1

print("insert data at the beginning")
data = 0
head = insert_at_begin(head, data)
output_linked_list_forward(head); print()

print("insert data at the tail")
data = 40
head = insert_at_tail(head, data)
output_linked_list_forward(head); print()

print("insert data at custom location")
data = 15; location = 3
head = insert_at_custom_location(head, data, location)
output_linked_list_forward(head); print()