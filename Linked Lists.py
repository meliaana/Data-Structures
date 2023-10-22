class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def insert_at_end(self, node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def delete_node(self, node):
        parent = self.find_parent_node(node)
        parent.next = node.next

    def find_node(self, node):
        current_node = self.head
        while current_node.val != node.val:
            if current_node.next is None:
                return None
            current_node = current_node.next
        return current_node

    def find_parent_node(self, node):
        current_node = self.head
        while current_node.next != node:
            if current_node.next is None:
                return None
            current_node = current_node.next
        return current_node
