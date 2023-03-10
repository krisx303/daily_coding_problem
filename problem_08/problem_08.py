class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self):
        return f"{self.val} -> {str(self.children)}"


root = Node(0)
leaf1 = Node(1)
leaf2 = Node(1)
leaf3 = Node(1)
leaf4 = Node(0)
node1 = Node(1)
node2 = Node(0)

node1.children = [leaf1, leaf2]
node2.children = [node1, leaf4]
root.children = [node2, leaf3]

global trees
trees = 0


def req(node: Node) -> bool:
    global trees
    if len(node.children) == 0:
        trees += 1
        return True
    count = 0
    for child in node.children:
        ret = req(child)
        if ret is True and child.val == node.val:
            count += 1
    if count == len(node.children):
        trees += 1
        return True
    return False


req(root)
print(trees)
trees = 0
