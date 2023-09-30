class Node:
    def __init__(self,val):
        self.elem=val
        self.right=None
        self.left=None
def find_depth(root):
    if root==None:
        return 0
    if root.left ==None and root.right==None:
        return 1
    if root.left==None:
        return 1+find_depth(root.right)
    if root.right==None:
        return 1+find_depth(root.left)
    return 1+ min(find_depth(root.left),find_depth(root.right))
    
    