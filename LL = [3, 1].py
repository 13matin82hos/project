LL = [3, 1]
sorted_LL = sorted(LL)
print(sorted_LL)  # Output: [1, 3]
LL = [5, 2, 4, 1, 3]
sorted_LL = sorted(LL)
print(sorted_LL)  # Output: [1, 2, 3, 4, 5]
import math
LL = [9, 6, 3, 8, 5, 2, 7, 4, 1]
m = math.ceil(2/3 * len(LL))
sorted_LL = sorted(LL[:m]) + LL[m:]
print(sorted_LL)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
