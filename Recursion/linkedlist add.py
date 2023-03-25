class Singly_Node:
    def __init__(self,elem):
        self.elem=elem
        self.next=None
def add_elem(head):
    if head ==None:
        return 0
    return head.elem+add_elem(head.next)
head=Singly_Node(1)
head.next=Singly_Node(2)
head.next.next=Singly_Node(3)
print(add_elem(head))