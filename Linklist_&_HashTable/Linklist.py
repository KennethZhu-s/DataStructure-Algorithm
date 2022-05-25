class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist_head(nums):
    head = Node(nums[0])
    for element in nums[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(nums):
    head = Node(nums[0])
    tail = head
    for element in nums[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next

lk = create_linklist_tail([1,2,3])
print_linklist(lk)