class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# output all data in linked list
temp = head
while temp is not None:
    print(temp.data, end=' ')
    temp = temp.next
print()

# common operations

# 1) run all through and check linked list
temp = head
target = 20; count = 0;
while temp is not None:
    count += 1
    if temp.data == target:
        print("found location of the data at", count)
        break
    temp = temp.next
    
# 2) insert linked list
    # at the beginning
    
new_head = Node(0)
new_head.next = head # connect to old linked list
temp = new_head
while temp is not None:
    print(temp.data, end=' ')
    # temp = new_head.next # make infinity loop because it just reset value of temp = new_head.next = head
    temp = temp.next # actually connect to real Node not value
print()

# -------------------------------------------------------------------------------------------------------------

    # at the end
    
new_Node = Node(40)

temp = head
while temp.next is not None:
    temp = temp.next
temp.next = new_Node

print(temp.data)
head = new_head
temp = head # reset to the same point
print(temp.data)
while temp is not None:
    print(temp.data, end=' ')
    temp = temp.next