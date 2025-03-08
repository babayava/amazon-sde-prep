# Implement a Queue using a Python List (Python's built-in list)
# pop(0) is O(n) thus this is not the most efficient implementation.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): #add item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) #remove and return the front item
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)





# **Testing the Queue**

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.front())
print(queue.is_empty())