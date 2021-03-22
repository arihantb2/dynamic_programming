# m = len(target)
# n = len(strings)
# time : O(n * m^2)
# space: O(m)

import numpy as np

def count_construct(target, strings):
    table = np.empty(len(target) + 1, dtype=int)
    table.fill(0)
    table[0] = 1

    for i in range(0, len(target) + 1):
        for string in strings:
            if target[i:].startswith(string):
                idx = i + len(string)
                if idx <= len(target):
                    table[idx] = table[idx] + table[i]

    return table[len(target)]


if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(count_construct('e'*25 + 'f', ['e'*i for i in range(1, 6)]))
