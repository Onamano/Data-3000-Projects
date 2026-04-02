from stack_interface import StackInterface

class StackImplementation(StackInterface):
    def _init_(self):
        """
        This method will serve as the constructor for the stack
        Uses list to store stack items
        END of list represents TOP of stack
        [10, 20, 30], 30 is the top item
        """
        self._stack = [] #creates empty list
        
    def push(self, new_entry):
        """
        This method adds a new entry to the top of the stack
        Uses append() to add new item
        """
        self._stack.append(new_entry)

    def pop(self): 
        """
        This will remove and returns the top item in stack
        LIFO, most recently added item is first one removed
        """
        if self.is_empty():#before removing we need to check if stack is empty
            raise IndexError("pop is from empty stack")#If it is, raise IndexError message
        
        return self._stack.pop()
    
    def peek(self):
        """
        This method returns the top item of the stack, doesn't remove it
        Sees top of stack but makes no changes
        """
        if self.is_empty():#before returning item, check if stack is empty
            raise IndexError("peek is from empty stack")#If it is raise error
        
        return self._stack[-1]#returns item from index -1
    
    def is_empty(self):
        """
        This method checks whether the stack has any items at all
        Returns: True = no items OR False = 0< items
        """
        return len(self._stack) == 0
    
    def clear(self):
        """
        This will clear the entire stack
        """
        self._stack.clear()