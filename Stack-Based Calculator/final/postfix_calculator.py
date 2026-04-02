from binary_search_tree import BinarySearchTree
from stack_implementation import StackImplementation

class PostfixCalculator:
    def __init__(self):
        """
        Constructor for the PostfixCalculator.
        Initializes two attributes:
          - self.variableTree: an instance of BinarySearchTree used for sotrage and retrieval of 
            variable keys and their integer values.
          - self.stack: An instance of StackImplementation used to hold operands and results
            during the evaluation process.
        """
        self.variableTree = BinarySearchTree()
        self.stack = StackImplementation()

    def set_variable(self, key, value):
        """
        Inserts a variable name (key) and its corresponding integer value
        into the binary search tree.
        """
        self.variableTree.insert(key, value) #calls insert method within the BST class to insert a key and value into the BST

    def delete_all_variables(self):
        """
        Clears all nodes from the variableTree to create a clean slate
        for the next postfix expression evaluation.
        """
        self.variableTree.delete_all() #calls delete_all method within BST class

    def evaluate_postfix_expression(self, expression):
        """
        Method to evaluate postfix expressions using a stack and a BST 
        to search for variables and their corresponding integer values.
        Expects an expression to be passed in.

        Logic:
        - Scan expression from left to right
        - if a number or variable is found, push its integer value into the stack
        - if an operator is found, pop the two most recent values, perform the operation,
          and push the result back into the stack
        - finally return the last remaining value in the stack (which is the final calculation of the expression)
        """
        self.stack.clear() #ensure stack is empty before starting a new evaluation by calling the clear method in the StackImplementation class
        input_values = expression.split() #split the postfix expression string passed in by spaces to get individual operands and operators and store in this list

        #now loop through each element in input_values list
        for element in input_values: 
            #check if the element is a digit while also handling negative numbers as isdigit() only returns true if the string contains only numeric characters
            #so if the first index of the current element string is '-' and from digit at index 1 on is a digit then we can catch the negative number and push it into the stack
            if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
                self.stack.push(int(element)) #call push method defined in StackImplementation class to add the element to the stack
            elif element in "+-*/": #and if the element is an operator
                
                b = self.stack.pop() #call pop method defined in StackImplementation class to pop the value at the top of the stack as 'b'
                a = self.stack.pop() #then pop the next value down from the stack as 'a'
                
                #now we can perfrom the operation of the operands based on the operator iin the expression
                if element == '+': result = a + b 
                elif element == '-': result = a - b
                elif element == '*': result = a * b
                elif element == '/': 
                    if b == 0: #check to make sure we are not dividing by 0
                        raise ZeroDivisionError("Devision by 0 is not allowed")
                    result = int(a / b)
                #after the calculation completes, push the new value back into the stack
                self.stack.push(result)

            #if the operand is a variable (a,b,c)
            else:
                val = self.variableTree.search(element) #use the search method defined in the BST class to search for that variable and its coresponding value
                if val is not None: #if a value is found
                    self.stack.push(val) #push it into the stack
                else: #if it is not found
                    raise ValueError(f"Variable '{element}' not found.") #raise an error
                
        #finally when all calculations have finished and there is only the final value left in the stack, pop it and return the value back to main
        return self.stack.pop() 