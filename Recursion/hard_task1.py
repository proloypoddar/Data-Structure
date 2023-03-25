class Node:
    def __init__(self, next, bottom, val):
        self.next = next
        self.bottom = bottom
        self.val = val

def flattenList(node, output_list):
    if node is None:
        return

    output_list.append(node.val)

    if node.bottom is not None:
        flattenList(node.bottom, output_list)

    flattenList(node.next, output_list)
n3 = Node(None, None,3)
n2 = Node(n3, None, 2)
n1 = Node(n2, None, 1)

output_list = []
flattenList(n1, output_list)
print(output_list) 