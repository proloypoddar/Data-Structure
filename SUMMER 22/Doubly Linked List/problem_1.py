class Node:
    def __init__(self,elem,next,prev):
        self.elem=elem
        self.next=next
        self.prev=prev
class DoublyLinked:
    def __init__(self,a):
        self.head=[Node(a[0],None,None)]
        cur=self.head
        for i in range(1,len(a)):
            Newnode=Node(a[i],cur,None)
            cur.next=Newnode
            Newnode.prev=cur
            cur=Newnode
        cur.next=self.head
        self.head.prev=cur
    def countNode(self):
        temp=self.head
        temp2=self.head.prev
        c=0
        while temp !=temp2:
            c+=1
            temp=temp.next
        return c
    def palindrome(self):
        temp=self.head
        temp2=temp.prev
        while temp!=temp2:
            if temp==temp2.next:
                return True
            return False
            temp=temp.next
        