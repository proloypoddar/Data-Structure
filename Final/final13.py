def balance(root):
    if root==None:
        return 
    left=height(root.left)
    right=height(root.right)
    if abs(left-right)>1:
        return False
    return balance(root.left) and balance(root.right)
def height(node):
    if node ==None:
        return 0
    left= height(node.left)
    right=height(node.right)
    return 1+max(left,right)