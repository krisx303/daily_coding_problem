## Problem 8 [Easy]
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

## Solution
We will be counting the number of unival tree by recursive function and global variable.

So recursive function gets node and: (returns if tree with given node as root is unival)
* when the given node has no children then it is a unival tree so we increase global variable and return True
* otherwise we count number of proper child trees:

    for each child we check if output is positive and value stored by child is the same as node value. If true, we increase count of valid child.
    if count of valid children is equals to number of children then we increase global variable