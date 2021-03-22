# m = target
# n = size(nums)
#
# Brute force:
# time : O(n^m)
# space: O(m) --- only includes call stack, does not include space used for return value (n^m)
#
# Memoized:
# time : O(n^m) --- cam't do any better than brute force because we have to represent all combinations in the output
# space: O(m) --- only includes call stack, does not include space used for return value (n^m)

def all_construct(target, strings, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return [[]]

    memo[target] = []
    for string in strings:
        if target.startswith(string):
            suffix = target[len(string):]
            suffixWays = all_construct(suffix, strings, memo)
            suffixWays = [[string] + way for way in suffixWays]
            memo[target] = memo[target] + suffixWays

    return memo[target]

if __name__ == '__main__':
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {}))
    print(all_construct('skateboard', [
          'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(all_construct('enterapotentpot', [
          'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
