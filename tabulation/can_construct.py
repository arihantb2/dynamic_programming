# m = len(target string)
# n = len(strings)
# Time : O(n * m^2)
# Space: O(m)

import numpy as np

def can_construct(target, strings):
    table = np.empty(len(target) + 1, dtype=bool)
    table.fill(False)
    table[0] = True

    for i in range(0, len(target) + 1):
        if table[i]:
            for string in strings:
                if target[i:].startswith(string):
                    idx = i + len(string)
                    if idx <= len(target):
                        table[idx] = True

    return table[len(target)]

if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(can_construct('e'*100 + 'f', ['e'*i for i in range(10)]))
