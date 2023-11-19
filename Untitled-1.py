def customized_sort(arr):
    if len(arr) <= 2:
        return sorted(arr)
    else:
        m = -(-2*len(arr)//3)  # ceiling division
        arr[:m] = customized_sort(arr[:m])
        arr[-m:] = customized_sort(arr[-m:])
        arr[:m] = customized_sort(arr[:m])
        return arr

# Example usage
my_list = [5, 3, 8, 2, 7, 1]
sorted_list = customized_sort(my_list)
print(sorted_list)