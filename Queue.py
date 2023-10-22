class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, element):
        # add element in the end
        self.queue.append(element)
        self.size += 1

    def pop(self):
        # Removes the first item
        first_element = self.top(self.queue)
        new_stack = self.queue[1: len(self.queue)]
        self.queue = new_stack
        self.size -= 1
        return first_element

    def top(self):
        # returns the first element
        return self.queue[0]

    def empty(self):
        if self.size == 0:
            return True
        return False

    def __len__(self):
        return self.size
