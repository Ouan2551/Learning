class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

data1 = Node(10)
data2 = Node(15); data1.next = data2
data3 = Node(20); data2.next = data3
data4 = Node(30); data3.next = data4
data5 = Node(40); data4.next = data5
data6 = Node(50); data5.next = data6

def delete_head(head):
    i = head
    if i is None:
        return None
    head = i.next
    return head

def delete_tail(head): #handle  empty linked list
    i = head
    if i is None:
        return None
    
    # find second last node
    while i.next.next is not None:
        i = i.next
    i.next = None
    
    return head

def delete_location(head, location):
    i = head
    if i is None:
        return None
    
    if location == 1:
        head = i.next
        return head
    
    for j in range(1, location, 1):
        i = i.next
        before_del = i
        after_del = i.next.next
    before_del.next = after_del
    return head

def output_linked_list(head):
    i = head
    while i is not None:
        print(i.data, end=' ')
        i = i.next

output_linked_list(data1)
print()

print("delete head")
head = delete_head(data1)
output_linked_list(head)
print()

print("delete tail")
head = delete_tail(head)
output_linked_list(head)
print()

print("delete specific location")
location = 3
head = delete_location(head, location)
output_linked_list(head)
print()