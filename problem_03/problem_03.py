
def find_missing_integer(array: list[int]) -> int:
    n = len(array)
    if n == 0:
        return 1
    for i in range(n):
        if array[i] == 0:
            array[i] = -1
    index = 0
    x = array[index]
    while index < n:
        if x < 1 or x > n:
            if index == n - 1:
                break
            index += 1
            x = array[index]
        else:
            buff = x - 1
            x = array[x - 1]
            array[buff] = 0
    print(array)
    for i in range(n):
        if array[i] != 0:
            return i + 1
    return n+1


arr = [3, 4, -1, 6, 8,  6, 9, 10, -3, -4, 12, 15, -2, -1, 16, 17, 20, 1, 2]
print(find_missing_integer(arr))

