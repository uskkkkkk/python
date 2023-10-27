class Node:
    def __init__(self, data):
        self.data = data  
        self.nref = None  
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.nref = self.start
            self.start.prev = new_node
            self.start = new_node

    def pop(self):
        if self.start is None:
            return IndexError

        pop_item = self.start
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None

        pop_item.nref = None
        val = pop_item.data

        return val

    def insert(self, n, val):
        node = Node(val)
        total = self.start
        count = 0
        while count < n and total:
            total = total.nref
            count += 1
        if total:
            node.next = total
            node.pref = total.pref
            if total.pref:
                total.pref.next = node
            else:
                self.start = node
            total.pref = node
        else:
            self.push(val)


    def print(self):
        total = self.end
        if self.end is None:
            return Exception
        else:
            while total:
                print(total.data)
                total = total.pref



queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.pop()
queue.insert(2,10000)
queue.print()
