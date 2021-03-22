# m = target
# n = len(numbers)
# Time : O(n * m^2)
# Space: O(m^2)

import numpy as np


def how_sum(target, numbers):
    table = np.empty(target+1, dtype=np.ndarray)
    table.fill(None)
    table[0] = np.empty(0, dtype=int)

    for i in range(0, target + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    new_list = np.append(table[i], num)
                    if (table[i + num] is None) or len(new_list) < len(table[i + num]):
                        table[i + num] = new_list


    return table[target]


if __name__ == '__main__':
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(8, [1, 4, 5]))
    print(how_sum(100, [1, 2, 5, 25]))
    print(how_sum(100, [25, 1, 5, 2]))
