class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# output linked list
def print_linked_list(head):
    i = head
    while(i is not None):
        print(i.data);
        i = i.next

def insert_linked_list_front(head, value):
    value.next = head
    head = value
    return head

def insert_linked_list_n_th(head, value, location):
    i = head
    for j in range(0, location-2, 1):
            i = i.next
    i.next = value; temp = i.next.next ;value.next = temp
    return head

data1 = Node(10)
data2 = Node(20); data1.next = data2
head = data1
print_linked_list(head)

value = Node(0)
head = insert_linked_list_front(head, value)
print_linked_list(head)

value = Node(15); location = 3
head = insert_linked_list_n_th(head, value, location)
print_linked_list(head)