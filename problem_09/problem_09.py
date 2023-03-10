array = [5, 13, 3, -2, 1, 9, -3]
n = len(array)
array[0] = max(0, array[0])
for i in range(1, n):
    prev = array[i-1]
    prevprev = 0
    if i > 1:
        prevprev = array[i-2]
    if array[i] < 0:
        array[i] = max(prev, prevprev)
    else:
        array[i] = max(prev, array[i] + prevprev)

print(array)
