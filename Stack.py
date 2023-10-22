class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, element):
        # add element at the top
        new_stack = [element]
        new_stack.extend(self.stack)
        self.stack = new_stack
        self.size += 1


    def pop(self):
        # remove element from the top and return pop-ed element
        last_element = self.top(self.stack)
        new_stack = self.stack[:len(self.stack) - 1]
        self.stack = new_stack
        self.size -= 1
        return last_element

    def top(self):
        # returns the top element
        return self.stack[-1]

    def empty(self):
        if self.size == 0:
            return True
        return False

    def __len__(self):
        return self.size















