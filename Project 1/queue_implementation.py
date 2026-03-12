from queue_interface import QueueInterface
from node import Node

#Class representing a queue, inherits from abstract based class
class QueueImplementation(QueueInterface):
    #Constructor for the queue
    def __init__(self):
        #Pointer to the first node in the queue
        self.front = None
        
        #Pointer to the last node in the queue
        self.back = None
        
        #Represents how many items are present in the queue
        self._length = 0

    #Method to add an element to the queue
    def enqueue(self, item):
        #Creates a new instance of the Node class
        new_node = Node(item)

        #If the queue is empty, sets both the front and back pointers to point to the new node (the new node would be the only element in the queue)
        if self.is_empty():
            self.front = self.back = new_node

        else:
            #Sets the next attribute of the current back pointer to the new node
            self.back.next = new_node
            
            #Sets the back pointer to the new node
            self.back = new_node
        
        #Increments the length of the queue by 1
        self._length += 1

    #Method to remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Cannot dequeue from empty queue")
        
        #Stores the data of the front element to return
        removed_data = self.front.data

        #Sets the next attribute of the current front pointer to the next element in the queue
        self.front = self.front.next

        #Sets the back pointer to None if the removed element was the only element in the queue
        if self.front is None:
            self.back = None

        #Decrements the size of the queue by 1
        self._length -= 1

        #Returns the front element of the queue
        return removed_data

    #Method for returning the front element of the queue
    def get_front(self):
        if self.is_empty():
            raise RuntimeError("Cannot get front element from empty queue")
        
        return self.front.data

    #Method for verifying if the queue is empty
    def is_empty(self):
        #Returns True if the front of the queue is None, returns False otherwise
        return self.front is None

    #Method for removing all elements from the queue
    def clear(self):
        self.front = None
        self.back= None
        self._length = 0
