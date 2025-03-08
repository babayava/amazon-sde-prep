# Implementing a Queue using Linked List
# dequeue() is O(1) thus more efficient //no shifting element like in list, dynamic mem alloc//
# we track both front and rear to optimize operations.
#if the queue becomes empty, we reset rear = None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # pointer to the next node

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node 
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def front_value(self):
        if not self.is_empty():
            return self.front.value
        return "Queue is empty"

    def is_empty(self):
        return self.front is None



#    **Testing the Queue**

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.front_value())
print(queue.is_empty())
