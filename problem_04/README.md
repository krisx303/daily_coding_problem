## Problem 4 [Medium]
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:
```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

## Solution
We use simple recursion for that problem, both for serialization and deserialization. Rest is just 'toString()' idea.

I assumed such format of node as string:
1. when it does not have children then it returns just its value.
2. otherwise it returns: 'value -> [child1, None]' or 'value -> [child1, child2]'

For example given node returns 'root -> [left -> [left.left, None], right]' as string.

So serialization is really easy, str method runs str method for each children and all is conected to one final string.

In the deserialization we must split our string and extract each node.
If given string does'n contain ' -> ', then there is only 2 options:
1. string is 'None' and we return just None value
2. we return Node without children, just with the string value

Otherwise we find index of ' -> ' and save that value as i.

Part of string from 0 to i is a value of node.

The second part is children array. And we are counting the number of opened brackets. (skip first '[')
When char is '[' we increase opened brackets and when char is ']' we decrease that number.

When number of opened brackets is equal to 0 and actual char is comma, then we found end of the left and right child.
So we just recursive run deserialize method for left and right child.
