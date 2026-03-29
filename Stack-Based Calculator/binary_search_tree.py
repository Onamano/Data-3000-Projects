from node import Node

class BinarySearchTree():
    #Initializes an empty tree
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        #If the tree is empty, the new node becomes the root
        if not self.root:
            self.root = Node(key, value)
        
        #If the tree is not empty, call insert_recursive to find the correct position to insert
        else:
            self.insert_recursive(self.root, key, value)

    #Method to navigate the tree to insert the node key-value pair
    def insert_recursive(self, node, key, value):
        #If the key is smaller go to the left
        if key < node.key:
            #If a left child exists move towards it
            if node.left:
                self.insert_recursive(node.left, key, value)
            
            #If there is no left child insert the new node
            else:
                node.left = Node(key, value)

        #If the key is larger go to the right
        elif key > node.key:
            #If a right child exists move towards it
            if node.right:
                self.insert_recursive(node.right, key, value)
            
            #If there is no right child insert the new node
            else:
                node.right = Node(key, value)

        #If the key matches, update the existing value
        else:
            node.value = value

    def search(self, key):
        return self.search_recursive(self.root, key)
    
    #Method using key comparison to narrow the search area
    def search_recursive(self, node, key):
        #If a key is not found return None, if a key is found return the corresponding value
        if not node or node.key == key:
            return node.value if node else None
        
        #If the key is smaller search to the left, otherwise search to the right
        if key < node.key:
            return self.search_recursive(node.left, key)
        return self.search_recursive(node.right, key)
    
    def delete(self, key):
        #Maintains tree structure if the root is deleted
        self.root = self.delete_recursive(self.root, key)

    #Method to reorganize tree after a node has been removed
    def delete_recursive(self, node, key):
        #If a key is not found return None
        if not node:
            return None
        
        #Navigate to the left if the key is smaller
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)

        #Navigate to the right if the key is larger
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)

        #Node is found if the key matches
        else:
            #If the node has no children or only one child, return existing child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            #If the node has two children, call method to find the smallest node in the right branch (successor)
            temp = self.min_value_node(node.right)

            #Copies the successor node data to the current node
            node.key, node.value = temp.key, temp.value

            #Deletes the successor node from the right branch of the tree
            node.right = self.delete_recursive(node.right, temp.key)

        return node
    
    #Method which returns the minimum value in a subtree
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    #Method which deletes the entire tree
    def delete_all(self):
        self.root = None

    #Method which prints the tree in alphabetaical order
    def display(self):
        self.in_order(self.root)
        print()

    #Method which orders the output from the tree
    def in_order(self, node):
        if node:
            #Visit everything smaller first
            self.in_order(node.left)
            
            #Visit the current node
            print(f"{node.key} : {node.value}", end = " | ")
            
            #Visit everything larger last
            self.in_order(node.right)
