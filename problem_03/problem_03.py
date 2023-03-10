class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return serialize(self)


node = Node('root', Node('left', Node('left.left')), Node('right'))


def serialize(node: Node) -> str:
    if node is None:
        return "None"
    if node.left is None and node.right is None:
        return str(node.val)
    return f"{node.val} -> [{serialize(node.left)}, {serialize(node.right)}]"


def deserialize(s: str) -> Node:
    if not s.__contains__(" -> "):
        if s == "None":
            return None
        return Node(s)
    index = s.index(" -> ")
    i = index + 5
    count = 0
    while True:
        if s[i] == ',' and count == 0:
            break
        elif s[i] == '[':
            count += 1
        elif s[i] == ']':
            count -= 1
        i += 1
    left = deserialize(s[index+5:i])
    right = deserialize(s[i+2:-1])
    return Node(s[:index], left, right)


assert deserialize(serialize(node)).left.left.val == 'left.left'
