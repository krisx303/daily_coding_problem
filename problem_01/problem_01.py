def find_2_elements_sum_up_to_k(array, k):
    s = set()
    for x in array:
        if (k - x) in s:
            return (k - x), x
        else:
            s.add(x)
    return None


print(find_2_elements_sum_up_to_k([10, 15, 3, 7], 17))
