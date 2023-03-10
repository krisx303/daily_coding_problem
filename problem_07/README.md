## Problem 7 [Medium]
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

## Solution
Used Dynamic Algorithm for storing number of ways the string can be decoded.

Assume n = lenght of given string.
Then we create the array with n ints.

Value at index i means how many ways exists in which we can decode part of string with length i. string[0:i].

array[0] = 1 because there is only one way to create empty string.

We iterate by index from 1 to n.
We can always decode message as actual letter (build from on digit) and connect message created by i-1 digits.
So array[i] += array[i-1]

When previous and actual digit create number smaller then 27 we can build 2 digit number and connect message created by i-2 digits.

So in this case array[i] += array[i-2].

This is the whole algorithm.