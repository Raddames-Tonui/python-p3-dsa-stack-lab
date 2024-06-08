# For Search trees
class Tree:   
    def __init__(self) -> None:
        self.root = None

class Node:
    def initialize(self, value):
        self.value = value
        self.children = []

# FOR BINARY TREE 
class Binary_tree:
    def __init__(self) -> None:
        self.root = None
    
class Binary_Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None