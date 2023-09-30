class Node:
    def __init__(self,val):
        self.elem=val
        self.right=None
        self.left=None
def full_node(root):
    if root is  None:
        return
    if root.left and root.right:
        print(root.elem)
    full_node(root.left)
    full_node(root.right)
root=Node(10)
root.left=Node(8)
root.right=Node(2)
root.left=Node(2)
root.right=Node(5)
root.left=Node(7)
full_node(root)