# m = target
# n = len(numbers)
# Time : O(n * m)
# Space: O(m)

import numpy as np

def can_sum(target, numbers):
    table = np.empty(target+1, dtype=bool)
    table.fill(False)
    table[0] = True

    for i in range(0, target + 1):
        if table[i] == True:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = True

    return table[target]

if __name__ == '__main__':
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(100, [7, 14]))
