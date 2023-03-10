## Problem 2 [Hard]
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

## Solution:
Let's take n as the length of given array.
1. Create new array with n elements.
2. For each element on index i calculate product of all elements on the left (at index 0,1,2 ... i) and save result to new array at position i.
   (You may achieve that in one pass by multiply previous product with current element).
3. Iterating from right to left, for each element again calculate product of all elements (this time on the right). 

## Pseudocode
```
given: array

n = length of array
temp_arr = empty array with length n

product = 1
for i in range(0, n):
   temp_arr[i] = product
   product = product * array[i]

product = 1
for i in range(n-1, 0):
   temp_arr[i] = temp_arr[i] * product
   product = product * array[i]
   
return temp_arr
```