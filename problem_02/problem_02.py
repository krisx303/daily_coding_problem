def calculate(array):
    n = len(array)
    temp_arr = [0]*n

    product = 1
    for i in range(n):
        temp_arr[i] = product
        product *= array[i]

    product = 1
    for i in range(n-1, -1, -1):
        temp_arr[i] *= product
        product *= array[i]

    return temp_arr


print(calculate([3, 2, 1, 5]))
