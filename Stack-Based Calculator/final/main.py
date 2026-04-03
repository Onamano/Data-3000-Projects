import tkinter as tk
from tkinter import messagebox
from postfix_calculator import PostfixCalculator

def main():
    """
    Main entry point for the postfix calculator program

    This program runs thorugh 8 different test cases and demonstrates the ability for
    the PostfixCalculator to be able to store variables in a binary search tree, 
    visualize that tree, and evaluate mathmatical expressions using a stack
    """
    root = tk.Tk() #initializes an instance of a tkinter root window which is needed for the welcome popup
    root.withdraw() #hides the main tkinter window, we only need to show popup dialogs

    #welcome message used for display in the initial program popup window
    welcome_message = (
        "A text based calculator that can evaluate arithmetic expressions "
        "in postfix notation using a stack data structure and handle variables "
        "using a binary search tree (BST).\n\n"
        "Press OK to Start"
    )
    #display a message showing purpose of program and asking the user to start the program 
    messagebox.showinfo("Welcome to", welcome_message)

    #initialize an instance of the calculator object
    calc = PostfixCalculator()

    #list of dictionaries containiing the 8 different test cases
    #each dict contains a key and value, notice the value of the vars key is another dictionary of keys and values
    test_cases = [
        {"expr": "x y * z +", "vars": {"x": 5, "y": 3, "z": 4}}, 
        {"expr": "a b + c *", "vars": {"a": 2, "b": 3, "c": 4}},
        {"expr": "m n * p -", "vars": {"m": 8, "n": 2, "p": 3}},
        {"expr": "q r s * +", "vars": {"q": 7, "r": 3, "s": 2}},
        {"expr": "d e f * + 4 +", "vars": {"d": 1, "e": 2, "f": 3}},
        {"expr": "g h i + * j /", "vars": {"g": 2, "h": 3, "i": 4, "j": 5}},
        {"expr": "k l + m n + *", "vars": {"k": 2, "l": 3, "m": 4, "n": 5}},
        {"expr": "o p / q r + * s +", "vars": {"o": 9, "p": 3, "q": 5, "r": 2, "s": 7}},
        #{"expr": "m a z + *", "vars": {"m": 10, "a": 5, "z": 2}} #example with left subtree
    ]

    #iterate through list of test case dictionaries starting counting at 1 instead of the default 0 for human readability, and for each 
    for i, case in enumerate(test_cases, 1):
        print("-" * 30) #print 30 dashes for separation between each case
        print(f"Postfix expression {i}: {case['expr']}") #print the current index(i) starting at 1 and the expression at that index (which the expression is a value to the "expr" key in the dict)
        
        #now for each key and value of the dictionary contained in the var keys value, 
        for var, val in case['vars'].items(): #.items() grabs both the key and value from the dictionary contained within the var keys value
            calc.set_variable(var, val) #call set_variable method within the postfix calculator to add the key and value into the BST

        #now display the BST for the current variables in the tree
        calc.variableTree.display_tree()

        #now call this method to evaluate the postfix expression using the stack and values from the BST
        result = calc.evaluate_postfix_expression(case['expr']) #store the calculation in result
        print(f"Result: {result}") #print the calculated result

        #delete all variables from the tree to prepare for the next set of test case variables
        calc.delete_all_variables() 
        print("Variables deleted.") 
        calc.variableTree.display_tree() #display tree again simply to confirm the tree is empty before moving on

if __name__ == "__main__": #runs the main program
    main()
