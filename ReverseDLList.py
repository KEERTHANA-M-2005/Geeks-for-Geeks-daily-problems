# You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

# Examples:

# Input:
   
# Output: 5 <-> 4 <-> 3
# Explanation: After reversing the given doubly linked list the new list will be 5 <-> 4 <-> 3.


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def ReverseDoublyLinkedList(head):
    temp = None
    curr = head
    
    while curr:
        # Swap prev and next
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        # Move to "next" node (which is prev after swapping)
        curr = curr.prev
    
    # New head will be last non-None node
    if temp:
        head = temp.prev
    
    return head

# 🔹 Helper: create DLL from list
def createDLL(arr):
    if not arr: return None
    head = DNode(arr[0])
    curr = head
    for val in arr[1:]:
        new_node = DNode(val)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head

# 🔹 Helper: print DLL
def printDLL(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "")
        temp = temp.next
    print()

# Example
head = createDLL([3, 4, 5, 6])
print("Original:")
printDLL(head)

res = ReverseDoublyLinkedList(head)
print("Reversed:")
printDLL(res)
