class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_linked_list(head, value):
    i = head; count = 0
    while i is not None:
        count += 1
        if i.data == value :
            return True, count
        i = i.next
    return False, "Not found the value"
def output_linked_list(head):
    i = head
    while i is not None:
        print(i.data, end=' ')
        i = i.next

data1 = Node('A')
data2 = Node('B'); data1.next = data2
data3 = Node('C'); data2.next = data3

head = data1
output_linked_list(head); print()

print("search linked list value and return location")
value = 'B'
location = find_check = None;
find_check, location = search_linked_list(head, value)
print("find or not : ", find_check)
print("location of value :", location)