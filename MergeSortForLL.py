# You are given the head of a linked list. You have to sort the given linked list using Merge Sort.

# Examples:

# Input:
    
# Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Explanation: After sorting the given linked list, the resultant list will be:

class Node:
    def __init__(self, head):
        self.head = None
        self.data = data 
    def MergeSort(self, head):
        if not head or not head.next:
            return head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next 
        slow.next = None
        return second 
    
    def Merge(l1, l2):
        if not l1:
            return l2 
        if not l2:
            return l1
        if l1.data < l2.data:
            l1.next = merge(l1.next, l2)
            return l1 
        else:
            l2.next = merge(l2.next,l1)
            return l2
    second = split(head)
    left = self.Mergesort(head)
    right = self.Mergesort(second)
    return Merge(left, right)