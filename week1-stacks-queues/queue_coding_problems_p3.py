""" Implement a Circular Queue """

""" A Circular Queue is a linear data structure that operates on the FIFO principle
but connects the end of the queue to the front, making it circular. """

"""   ** circular movement is handled using   (rear + 1) % size    """

""""  ***    if (rear + 1) % size == front:   # this condition ensures that 
                                 # we DO NOT OVERWRITE existing elements when queue is full.
                                 # it efficiently handles circular behavior by wrapping around the index. """


## TASK: Implement a circular queue with the following methods:  ##

class CircularQueue():
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    
    # 1. Check if the queue is full.
    # 2. Handle the first element correctly
    # 3. Move rear correctly.
    # 4. Insert the value into queue 
    # 5. Return true after successfully inserting.
    def enqueue(self, value):

        if (self.rear +1) % self.size == self.front:  # check if queue is full
            return False                              # queue is full
       
       # If inserting first element
        if self.front == -1:                         # if empty                     
            self.front = 0                           # set front = 0 before inserting the first element
        self.rear = (self.rear +1) % self.size       # move rear to the next position
        self.queue[self.rear] = value

        return True



    # This method correctly handles 
    #    - empty queues, 
    #    - normal cases, and 
    #    - circular wrap-around
    def dequeue(self):
        if self.front == -1:  # check if empty
            return False      # queue is empty, nothing to dequeue
        
        if self.front == self.rear:      # only one ele left in the queue
            self.front = self.rear = -1  # reset queue to the empty state
        else:
            self.front = (self.front + 1) % self.size    # we need % by size to ensure it wraps back when reaching the size of the queue
        
        return True   # Dequeue successful!!


    """Returns the front element of the queue or -1 if empty"""
    def get_front(self):
        return -1 if self.front == -1 else self.queue[self.front]


    """Returns the rear element of the queue or -1 if empty"""
    def get_rear(self):
        return -1 if self.rear == -1 else self.queue[self.rear]


    def empty(self):
        return self.front == -1


    def full(self):
        return (self.rear +1) % self.size == self.front


    
""" Test the Queue """

q = CircularQueue(5)
print(q.enqueue(1))
print(q.enqueue(20))
print(q.enqueue(15))
print(q.get_front())
print(q.get_rear())
print(q.dequeue())
print(q.get_rear())
print(q.get_front())
print(q.full())
print(q.empty())
print(q.enqueue(21))
print(q.enqueue(22))
print(q.enqueue(23))
print(q.get_rear())
print(q.enqueue(24))
print(q.full())