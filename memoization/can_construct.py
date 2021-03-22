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

def can_construct(target, strings, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True

    memo[target] = False
    for string in strings:
        if target.startswith(string):
            suffix = target[len(string):]
            if can_construct(suffix, strings, memo):
                memo[target] = True
                break

    return memo[target]


if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(can_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(can_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(can_construct('e'*100 + 'f', ['e'*i for i in range(10)], {}))
