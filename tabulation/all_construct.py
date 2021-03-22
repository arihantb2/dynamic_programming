# m = len(target)
# n = len(strings)
# Time : O(n^m) --- cam't do any better than brute force because we have to represent all combinations in the output
# Space: O(m) --- only includes call stack, does not include space used for return value (n^m)

import numpy as np

def all_construct(target, strings, memo={}):
    table = {}
    table[0] = [[]]
    for i in range(1, len(target) + 1):
        table[i] = []

    for i in range(0, len(target) + 1):
        for string in strings:
            if target[i:].startswith(string):
                idx = i + len(string)
                if idx <= len(target) and len(table[i]) > 0:
                    combinations = [comb + [string] for comb in table[i]]
                    if len(table[idx]) == 0:
                        table[idx] = combinations
                    else:
                        table[idx] = table[idx] + combinations

    return table[len(target)]


if __name__ == '__main__':
    print(all_construct('abcdef', ['ab', 'abc',
          'cd', 'def', 'abcd', 'ef', 'c'], {}))
    print(all_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(all_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
