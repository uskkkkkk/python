class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index):
        if self.head is None:
            return None
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None

    def remove(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            count = 0
            while current is not None and count < index-1:
                current = current.next
                count += 1
            if current is None or current.next is None:
                return
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        elif n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current is not None and count < n-1:
                current = current.next
                count += 1
            if current is None:
                return
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)

for item in linked_list:
    print(item)  

print(linked_list.get(1))  

linked_list.remove(1)
for item in linked_list:
    print(item)  

linked_list.insert(1, 2)
for item in linked_list:
    print(item)  
