class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, obj_val):
        self.head = Node(obj_val)

    def insert_at_beginning(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    def insert_at_end(self, value):
        # @TODO: question more complex then insert at start?
        current_node = self.head
        if self.valueEquals(current_node, value):
            raise KeyError(f'{value[0]} already exists')
        while current_node.next is not None:
            if self.valueEquals(current_node, value):
                raise KeyError(f'{value[0]} already exists')
            current_node = current_node.next
        current_node.next = Node(value)

    def delete_node(self, value):
        find_node = self.find_node(value)
        if find_node is None:
            raise KeyError
        parent = self.find_parent_node(value)
        if parent:
            parent.next = find_node.next
        else:
            # If parent doesnt not exist we are deleting first element
            self.head = self.head.next

    def find_node(self, node):
        current_node = self.head
        if current_node is None:
            raise KeyError
        # @TODO: question: time complexity is O(n) - ?
        while current_node.val != node:
            if current_node.next is None:
                return None
            current_node = current_node.next
        return current_node

    def find_parent_node(self, node):
        current_node = self.head
        if current_node.val == node:
            return None
        while True:
            if current_node.next is None:
                return None
            if current_node.next.val == node:
                return current_node
            current_node = current_node.next

