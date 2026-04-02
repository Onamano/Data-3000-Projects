from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push(self, new_entry):
        """
        Adds a new entry to the top of the stack
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Removes and returns the top entry of the stack.
        :raises IndexError: If the stack is empty
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Retrieves the top entry of the stack.
        :raises IndexError: If the stack is empty
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Removes all entries from this stack.
        """
        pass