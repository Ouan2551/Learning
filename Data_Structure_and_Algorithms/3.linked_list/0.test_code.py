class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_to_front(head, x):
    new_data = Node(x)
    new_data.next = head
    return new_data

def add_to_tail(head, x):
    new_data = Node(x)
    i = head
    while i.next is not None:
        i = i.next
    i.next = new_data
    return head

def add_to_position(head, x, position):
    i = head; data_after_position = None
    new_data = Node(x)
    for j in range(1, position-1, 1):
        i = i.next
        data_after_position = i.next
    i.next = new_data
    i = i.next
    i.next = data_after_position
    return head

def output_linked_list(head):
    i = head
    while i is not None:
        print(i.data, end=' ')
        i = i.next

head1 = Node(10)
head2 = Node(20)
head3 = Node(30)


head1.next = head2
head2.next = head3

i = head1
while i is not None:
    print(i.data, end=' ')
    i = i.next

print()
print("Add new data to the front")

data = 0
head = head1
head = add_to_front(head, data)
output_linked_list(head)

print()
print("Add new data to the tail")

data = 40
head = add_to_tail(head, data)
output_linked_list(head)

print()
print("Add data to specific location")

data = 15 # place between 10 and 20 that's 3th
position = 3
add_to_position(head, data, position)

output_linked_list(head)
print()