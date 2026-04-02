from node import Node
from binary_search_tree import BinarySearchTree

class Stack_calculator():
    def evaluatePostfixExpressions(self, expression):
        # Initializing an array to hold the elements of the stack
        stack = arrayStack

        # Split by spaces to handle multi-digit numbers and variables
        inputValues = expression.split()

        # Evaluating each element and appending it to the stack if it is a number 
        # Performing the calculation of the first 2 numbers in the stack if it is an operator
        for element in inputValues:
            # Appends the element to the stack if the element is a number
            if element.isdigit():
                stack.append(int(element))
            
            # Checks if the element is an operator 
            # If so it pops the first two elements of the stack and performs the calculation based on the operator
            else:
                b = stack.pop()
                a = stack.pop()
                
                if element == '+':
                    stack.append(a + b)
                elif element == '-':
                    stack.append(a - b)
                elif element == '*':
                    stack.append(a * b)
                elif element == '/':
                    stack.append(a / b)
        
        # Returns final value of the stack after all the operations have been completed
        return stack[0]
