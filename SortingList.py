# Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

# Examples:

# Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2

# Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2
# Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between. The final list will be:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def seggregateList(head):
        if not head or not head.next:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.data)
            cur = cur.next
        
        arr.sort()
        
        cur = head
        for i in range(len(arr)):
            cur.data = arr[i]
            cur = cur.next 
            
        return head
    
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(0)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(2)

    head = Solution.seggregateList(head)

    while head:
        print(str(head.data), end="")
        if head.next != None:
            print(" -> ", end="")
        head = head.next
    print()