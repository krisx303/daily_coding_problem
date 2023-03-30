## Problem 15 [Medium]

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

## Solution

Assume that 1/4 of incoming stream (of numbers for example) will fit in memory, so each element of stream put in collection with probability 1/4. (probably best collection will be Linked List).

When amount of elements will be too big to store in memory. Remove each element with probability 50%. Then incoming numbers will be stored with probability of 25% * 50% = 12.5%.

Repeat that whenever there will be no space to store next number.