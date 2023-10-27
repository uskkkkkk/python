class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    
    def __init__(self):
        self.next = None

    def push(self, data):
        
        new_node = Node(data)

        if self.next is None:
            self.next = new_node
        else:
            new_node.pref = self.next
            self.next = new_node

        pass

    def pop(self):
        
        if self.pref is None:
            return IndexError
        
        pop_item = self.pref
        self.pref = self.pref.next
        pop_item.next = None
        return pop_item.data

    def print(self):
        total = self.next
        if self.next is None:
            return Exception
        else:
            while total:
                print(total.data)
                total = total.pref

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
