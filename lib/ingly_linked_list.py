class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class Linked_list:
    def __init__(self, head=None) -> None:
        self.head = head

    def append_node(self, node):
        # Add element to the beginning of the list if the list is empty
        if self.head is None:
            self.head = node
            return
        # Otherwise, traverse the list to find the last node
        last_node = self.head
        while last_node.next_node is not None:
            last_node = last_node.next_node
        last_node.next_node = node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        prev_node = None
        while current_node is not None and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next_node
        if current_node is None:
            print(f"Node with data {key} not found.")
            return
        if prev_node is None:
            self.head = current_node.next_node
        else:
            prev_node.next_node = current_node.next_node
        print(f"Node with data {key} deleted.")

# Example usage
# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Creating the linked list and appending nodes
linked_list = Linked_list()
linked_list.append_node(node1)
linked_list.append_node(node2)
linked_list.append_node(node3)

# Printing the list
linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None

# Inserting a node at the beginning
linked_list.insert_at_beginning(0)
linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Deleting a node
linked_list.delete_node(2)
linked_list.print_list()  # Output: 0 -> 1 -> 3 -> None
