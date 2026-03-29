class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    curr = head; prev = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        head = prev
    return head

def output_linked_list(head):
    i = head
    while i is not None:
        print(i.data, end=' '); i = i.next

data1 = Node('a');
data2 = Node('b'); data1.next = data2
data3 = Node('c'); data2.next = data3

print("reverse_linked_list")
head = reverse_linked_list(data1)
output_linked_list(head); print()