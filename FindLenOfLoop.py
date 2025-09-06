# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

# Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

# Examples:

# Input: pos = 2,
# Output: 4
# Explanation: There exists a loop in the linked list and the length of the loop is 4.    


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class Solution:
    def LengthofLoop(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast:
                return self.countNodes(slow)
        return 0
    
    def countNodes(self, node):
        count = 1
        temp = node.next  
        while temp != node:
            count += 1
            temp = temp.next 
        return count 
    
if __name__ == "__main__":
    
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.next.next.next.next.next = head.next

    ob = Solution()
    res = ob.LengthofLoop(head)
    print(res)