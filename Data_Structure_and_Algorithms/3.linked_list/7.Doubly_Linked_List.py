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

def output_linked_list_backward(tail):
    i = tail
    while i is not None:
        print(i.data, end=' ')
        i = i.prev

data1 = Node(10)
data2 = Node(20); data1.next = data2; data2.prev = data1
data3 = Node(30); data2.next = data3; data3.prev = data2

output_linked_list_forward(data1); print()
output_linked_list_backward(data3); print()