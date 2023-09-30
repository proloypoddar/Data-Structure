def find_ancestoer(root,key):
    if root==None:
        return 
    if root.val==key:
        return True
    if find_ancestoer(root,root.left):
        print(root.val)
        return True
    if find_ancestoer(root,root.right):
        print(root.val)
        return True
    return False