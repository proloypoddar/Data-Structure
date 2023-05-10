class Node:
    def __init__(self,val):
        self.elem=val
        self.right=None
        self.left=None
def sked(root):
    if root== None:
        return "Yes"
    if root.left !=None and root.right !=None:
        return "No"
    return sked(root.left)and sked(root.right)
    