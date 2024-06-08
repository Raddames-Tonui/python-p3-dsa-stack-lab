class Tree:
    def __init__(self, root):
        self.root = root

    def breadth_first_traversal(self):
        if not self.root:
            return []
        
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)  # Pop the first element (FIFO)
            result.append(current_node['value'])
            nodes_to_visit.extend(current_node.get('children', []))  # Add children to the end of the list
        
        return result

class DepthTree:
    def __init__(self, root):
        self.root = root

    def depth_first_traversal(self):
        if not self.root:
            return []
        
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)  # Pop the first element (LIFO due to prepend operation below)
            result.append(current_node['value'])
            nodes_to_visit = current_node.get('children', []) + nodes_to_visit  # Add children to the front of the list
        
        return result

# Define the tree structure
tree_data = {
    'value': 1,
    'children': [
        {
            'value': 2,
            'children': [
                {'value': 4, 'children': []},
                {'value': 5, 'children': []}
            ]
        },
        {
            'value': 3,
            'children': [
                {'value': 6, 'children': []},
                {'value': 7, 'children': []}
            ]
        }
    ]
}

alphabet_tree = {
    'value': 'a',
    'children': [
        {
            'value': 'b',
            'children': [
                {'value': 'd', 'children': []},
                {'value': 'e', 'children': []}
            ]
        },
        {
            'value': 'c',
            'children': [
                {'value': 'f', 'children': []},
                {'value': 'g', 'children': []}
            ]
        }
    ]
}

# Create Tree objects
tree = Tree(tree_data)
alphabet_tree_traversal = Tree(alphabet_tree)

# Perform breadth-first traversal
result = tree.breadth_first_traversal()
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]

alphabet_traversal_result = alphabet_tree_traversal.breadth_first_traversal()
print(alphabet_traversal_result)  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Create DepthTree objects
depth_tree = DepthTree(tree_data)
depth_alphabet_tree_traversal = DepthTree(alphabet_tree)

# Perform depth-first traversal
depth_result = depth_tree.depth_first_traversal()
print(depth_result)  # Output: [1, 2, 4, 5, 3, 6, 7]

depth_alphabet_traversal_result = depth_alphabet_tree_traversal.depth_first_traversal()
print(depth_alphabet_traversal_result)  # Output: ['a', 'b', 'd', 'e', 'c', 'f', 'g']




class Tree:
    def __init__(self, root=None):
        self.root = root

  # ------------------------ USING DEPTH --------------------------
    # def get_element_by_id(self, id):
    #     if not self.root:
    #         return None  # Return None if the tree is empty

    #     nodes_to_visit = [self.root]

    #     while nodes_to_visit:
    #         current_node = nodes_to_visit.pop(0)  # Pop the first element (LIFO for DFS when combined with prepend operation)
    #         if current_node['id'] == id:
    #             return current_node  # Return the node if its id matches the given id
    #         nodes_to_visit = current_node.get('children', []) + nodes_to_visit  # Prepend children to the front of the list
        
    #     return None  # Return None if no node with the given id is found
    

    # # ----------------USING BREADTH ---------------------------
    def get_element_by_id(self, id):
        if not self.root:
            return None
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            if current_node['id'] ==id:
                return current_node
            nodes_to_visit = nodes_to_visit + current_node.get('children', [])

        return None

# Define the tree structure with 'id' attribute
tree_data = {
    'id': 1,
    'value': 'a',
    'children': [
        {
            'id': 2,
            'value': 'b',
            'children': [
                {'id': 4, 'value': 'd', 'children': []},
                {'id': 5, 'value': 'e', 'children': []}
            ]
        },
        {
            'id': 3,
            'value': 'c',
            'children': [
                {'id': 6, 'value': 'f', 'children': []},
                {'id': 7, 'value': 'g', 'children': []}
            ]
        }
    ]
}

# Create a Tree object
tree = Tree(tree_data)

# Get element by id
element = tree.get_element_by_id(5)
print(element)  # Output: {'id': 5, 'value': 'e', 'children': []}

element = tree.get_element_by_id(8)
print(element)  # Output: None (since there is no node with id 8)


