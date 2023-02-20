## Problem 1 [Easy]
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## Solution:
1. Create a Set of Integers (preferably HashSet for the best performance).
2. For each element (x) of list do:
    * If number (k - x) does not exists in Set then add x to Set
    * Otherwise return x and (k - x) because they add up to k
3. If the iteration is over, there are no such items in the list.

## Pseudocode
```
given: array, k
set = Set()
for x in array:
    if (k - x) is in set:
        return (k - x) and x
    else:
        add x to set
return null
```