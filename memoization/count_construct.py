# m = target
# n = size(nums)
#
# Brute force:
# time : O(n^m * m)
# space: O(m^2)
#
# Memoized:
# time : O(n * m^2)
# space: O(m^2)

def count_construct(target, strings, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return 1

    memo[target] = 0
    for string in strings:
        if target.startswith(string):
            suffix = target[len(string):]
            memo[target] = memo[target] + count_construct(suffix, strings)

    return memo[target]


if __name__ == '__main__':
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(count_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(count_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(count_construct('e'*100 + 'f', ['e'*i for i in range(10)], {}))
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
