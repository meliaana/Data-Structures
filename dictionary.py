from LinkedLists import LinkedList

class MyTuple:
    def __init__(self, first, secod):
        self.first = first
        self.second = secod

    def __eq__(self, other):
        return self.first == other.first


class Dictionary:
    def __init__(self, n):
        self.data_list = [None] * n
        self.n = n
        self.size = 0

    def gethash(self, key):
        return hash(key) % self.n

    def __setitem__(self, key, value):
        key_hash = self.gethash(key)
        if self.data_list[key_hash] is None:
            self.data_list[key_hash] = LinkedList(MyTuple(key, value))  # create linked list with val = [key, value]
        else:
            self.data_list[key_hash].insert_at_beginning(MyTuple(key, value))  # add new Node([key, val]) to linked list
        self.size += 1

    def __getitem__(self, key):
        key_hash = self.gethash(key)
        if self.data_list[key_hash] is None:
            raise KeyError(f'{key} not found')
        else:
            return self.data_list[key_hash].find_node(MyTuple(key, None)).val.second

    def __delitem__(self, key):
        key_hash = self.gethash(key)
        if self.data_list[key_hash] is None:
            raise KeyError(f'{key} not found')
        else:
            self.data_list[key_hash].delete_node(MyTuple(key, None))
            self.size -= 1

    def __len__(self):
        return self.size


a = Dictionary(5)
a['ana'] = 24
a['amiran'] = 27
a['salome'] = 28
a['babi'] = 7
a['io'] = 9
a['nino'] = 15
print(a['ana'], a['amiran'], a['salome'], a['babi'], a['io'], a['nino'])
del a['salome']
print(a)
print(a['salome'])
