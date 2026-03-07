from abc import ABC, abstractmethod

class QueueInterface(ABC):
    """
    Represents a queue interface
    """

    @abstractmethod
    def enqueue(self, new_entry):
        """
        Adds new entry to the back of the queue
        :param new_entry An object to be added
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Removes and returns the entry at the front of the queue.
        return The object at the front of the queue.
        raises RuntimeError if the queue is empty before the operation.
        """
        pass

    @abstractmethod
    def get_front(self):
        """
        Retrieves the entry at the front of the queue.
        Return the object at the front of the queue.
        Raises RuntimeError if the queue is empty.
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks whether the queue is empty
        Returns True if the queue is empty, False otherwise.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Removes all entries from the queue.
        """
        pass