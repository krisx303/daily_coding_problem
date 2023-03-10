## Problem 3 [Hard]
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

## Solution:
Let's take n as the length of given array. We will be using the given array as a container for information which numbers
in range 1...n+1 are present. So when array[2] is 0 (in python it can be True for better understand) it means that there is number (2+1)=3 in input array.
We add 1 to this number because we don't care about information if 0 is stored in array.

If we mark present numbers as 0 value we must replace all zeros in array firstly. In other way algorithm won't work properly.
Of course this operation has O(n) complexity.

Let's take x as array[0] and i as 0. If x is 0 or negative number or it is bigger then n then we simply ignore it and go to the next 
value (i=i+1 and x = array[i]). But otherwise we will jump to position stored in x (x - 1 for real) (we only change x, i will be the same as before). In the same time we must get a next value of x and replace number in array to 0.
If value after jump is 0 then x=array[i].
We end algorithm if value of i will be greater then n-1.

### For example:
Assume: array = [3, 4, -1, 1]

On the start: i=0 and x=array[0]=3

Value of x satisfy our second conditional so we jump to the index 3-1=2.

x = array[2] and after that we mark 3 as present value so array[2] = 0. ([3, 4, 0, 1], x=-1, i=0)

x is out of bound so we increase i and get x = array[i] = array[1] = 4

We jump to index 4-1=3.

x = array[3] and we mark 4 as present ([3, 4, 0, 0], x=1, i=1)

We jump to index 1-1=0.

x = array[0] and we mark 1 as present ([0, 4, 0, 0], x=3, i=1)

we jump to index 3-1=2 and then to index 4-1=3 but then x (x=0) is out of bound so we skip and skip again. It is end of array.

On the end we iterate from start to end and we are searching the number other then 0. So in this case answer is 2

In next iteration we mark 1 as present 
## Pseudocode
```
replace all zeros in given array
i = 0
x = array[0]
while i < n do:
    if x is out of the bound:
        if i == n - 1 (there is no next value):
            break loop
        i++
        x = array[i]
    else:
        prev_x = x
        x = array[x - 1]
        mark array[prev_x - 1] (set as 0 or True)

find first non 0 value in array and return its index + 1     
```