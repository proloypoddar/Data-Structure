class Singly_Node:
    def __init__(self,elem):
        self.elem=elem
        self.next=None
def reverse(head):
    if head==None:
        return 0
    reverse(head.next)
    print(head.elem)
head=Singly_Node(10)
head.next=Singly_Node(20)
head.next.next=Singly_Node(30)
head.next.next.next=Singly_Node(40)
reverse(head)--