## Problem 12 [Hard]
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1

2, 1, 1

1, 2, 1

1, 1, 2

2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

## Solution

Algorithm dymanicly (iterational).

Create an array with size N+1 with zeros.

array[i] = number of ways in which we can climb up to i level.

For each stair (staring from 1) check each possible step if you could jump from i-step level to current level. If yes, then add value at i-step position.
