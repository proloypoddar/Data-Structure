class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.tail is None:
            return None
        elem = self.tail.elem
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return elem
    
    def peek(self):
        if self.tail is None:
            return None
        return self.tail.elem
    def is_empty(self):
        return self.head is None
def prob(idx, x):
    s = Stack()
    index = 0
    for i in x:
        while index <= idx and (s.is_empty() or s.peek() != x[index]):
            s.push(i)
            break
        while not s.is_empty() and s.peek() == x[index]:
            s.pop()
            index += 1
            if index == idx:
                return False
    return True
def check(idx, array):
    if prob(idx, array):
        return "No"
    else:
        return "Yes"
length = 5
array = [5, 1, 2, 4, 3]
print(check(length, array))  
