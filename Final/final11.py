def single_child(root):
    if root==None:
        return root
    if root.left is None and root.right is not None:
        print(root.val)
    if root.left is not None and root.right is None:
        print(root.val)
    return single_child(root.left) and single_child(root.right)