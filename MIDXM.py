# # class Node:
# #     def __init__(self,a,n):
# #         self.elem=a
# #         self.next=n
# # class LinkedList_Stack:
# #     def __init__(self):
# #         self.head=None
# #     def push(self,a):
# #         if self.head==None:
# #             self.head=Node(a,None)
# #             return self.head
# #         else:
# #             newnode=Node(a,None)
# #             newnode.next=self.head
# #             self.head=newnode
# #     def pop(self):
# #         if self.head==None:
# #             return None
# #         else:
# #             x=self.head
# #             self.head=x.next
# #             return x.elem
# #     def peek(self):
# #         if self.head==None:
# #             return None
# #         else:
# #             self.head.elem


# # def find_largest_node(head):
# #     temp=head.next
# #     temp2=temp.next
# #     c=0
# #     while temp2 !=temp:
# #         if temp2.data>=c:
# #             print(temp2.data)
# #         else:
# #             c=temp2.data
# #         temp2=temp2.next
# #     return c


# class Stack:
#     def __init__(self):
#         self.item=[]
#     def pop(self):
#         if len(self.item)!=0:
#             a=self.item[len(self.item)-1]
#             self.item=self.item[:len(self.item)-1]
        
#             return a
#     def push(self,a):
#         self.item=self.item+[a]
#     def empty(self):
#         return len(self.item)==0

# def reverse(a):
#     s=Stack()
#     for i in a:
#         s.push(i)
#     rev=""
#     while not s.empty():
#         rev+=s.pop()
#     print(rev) 
# reverse("CSE220")
class Node:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next

class LinkedList:
    def __init__(self,a):
        self.head=a
    def move_last(self):
        last=self.head
        second_last=None
        while last.next:
            second_last=last
            last=last.next
        second_last.next=None
        last.next=self.head
        self.head=last
        return self.head 


def even_odd_linked_list(head):
    temp=head
    while temp !=None:
        if temp.elem%2==0:
            even=Node(temp.elem,None)
            even.next=even
        else:
            odd=Node(temp.elem,None)
            odd.next=odd
        temp=temp.next
        even.next=odd
        return even
