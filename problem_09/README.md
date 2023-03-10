## Problem 9 [Hard]
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

## Solution
This simple idea is based on choosing or not choosing actual number.

We will modify given array to store largest sum of non-adjacent numbers at indexes from 0 to i where 0<=i<n.

First element is simpy because if it is not negative we always choose that number so: array[0] = maximum(0, array[0]).
For each next element we set two new variables:
* prev which is just prevoius value in array (array[i-1])
* second_prev which is second prevoius value in array or 0 if i equals 1

When actual value is negative we choose maximum from prev and second_prev,
otherwise we must incldue actual value so: array[i] = maximum(prev, array[i] + second_prev).