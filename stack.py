"""
ASSIGNMENT 5
---------------------
NAME: POLOK PODDAR
ID:21301644
SEC:02
----------------------

"""

"""Solve the above problem using an array based stack."""
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items += [item]

    def pop(self):
        if not self.is_empty():
            item = self.items[-1]
            self.items = self.items[:-1]
            return item

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        count = 0
        for i in self.items:
            count += 1
        return count

def balance(a):
    s = Stack()
    error = False
    for i in range(len(a)):
        if a[i] in ("(", "{", "["):
            s.push(a[i])
        elif a[i] in (")", "}", "]"):
            if s.is_empty():
                error = True
                break
            elif (a[i] == ")" and s.peek() == "(") or \
                    (a[i] == "}" and s.peek() == "{") or \
                    (a[i] == "]" and s.peek() == "["):
                s.pop()
            else:
                error = True
                break
    if not s.is_empty() or error:
        print("This expression is NOT correct.")
    else:
        print("This expression is correct.")
x="1+2*(3/4)"
balance(x)

# """Solve the above problem using a linked list based stack."""
class Node:
    def __init__(self, elem,none):
        self.elem=elem
        self.next=none
class Stack:
    def __init__(self):
        self.top=None
    def push(self,elem):
        new_node=Node(elem,None)
        new_node.next=self.top
        self.top=new_node
        return self.top
    def pop(self):
        if self.top==None:
            return "Under Flow"
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.elem
    def peek(self):
        if self.top==None:
            return None
        return self.top.elem
def balance(a):
    s=Stack()
    error=False
    for i in range(0,len(a)):
        if (a[i]) == "(" or (a[i]) == "{" or (a[i]) == "[":
                s.push(a[i])
        elif (a[i]) == ")":   
            if s.top == None:
          
                error=True
                break
            elif (s.peek()) == "(":
                s.pop()
            else:
                error=True
                break  
        elif (a[i]) == "}":
            if s.top == None:
          
                error=True
                break
            elif (s.peek()) =="{":
                s.pop()
            else:
                error=True
                
                break
        elif (a[i]) == "]":
            if s.top == None:
               
                break
            elif (s.peek()) =="[":
                s.pop()
            else:
               
                error=True
                break
    chk=False
    if s==None:
        chk=True
    else:
        chk=False
        
    if error == False or chk == True:
        print('This expression is correct.')
    else:
        print('This expression is NOT correct.')    
# x=Stack()
# x.push(7)
# x.push(1)
# x.push(2)
# x.push(3)
# x.pop()
# print(x.peek())

x="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
balance(x)



