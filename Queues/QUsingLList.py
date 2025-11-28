# Implement a Queue using a Linked List, this queue has no fixed capacity and can grow dynamically until memory is available.
# The Queue must support the following operations:

# (i) enqueue(x): Insert an element x at the rear of the queue.
# (ii) dequeue(): Remove the element from the front of the queue.
# (iii) getFront(): Return front element if not empty, else -1.
# (iv) isEmpty(): Return true if the queue is empty else return false.
# (v) size(): Return the number of elements currently in the queue.

# There will be a sequence of queries queries[][]. The queries are represented in numeric form:

# 1 x : Call enqueue(x)
# 2: Call dequeue()
# 3: Call getFront()
# 4: Call isEmpty()
# 5: Call size()
# You just have to implement the functions enqueue, dequeue, getFront,  isEmpty and size. The driver code will handle the input and output.

# Node class
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.front is None

    def enqueue(self, x):
        # Add element x to the rear
        newNode = Node(x)
        if self.rear is None:       # Queue is empty
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.length += 1

    def dequeue(self):
        # Remove the front element
        if self.isEmpty():
            return -1     # Or return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:      # Queue becomes empty
            self.rear = None

        self.length -= 1
        return temp.data

    def getFront(self):
        # Return front element, -1 if empty
        if self.isEmpty():
            return -1
        return self.front.data

    def size(self):
        return self.length
