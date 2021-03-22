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


def best_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    memo[target] = None
    for num in nums:
        rem = target - num
        result = best_sum(rem, nums, memo)
        if result is not None:
            combination = result + [num]
            if (memo[target] is None) or (len(combination) < len(memo[target])):
                memo[target] = combination

    return memo[target]


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7], {}))
    print(best_sum(8, [2, 3, 5], {}))
    print(best_sum(8, [1, 4, 5], {}))
    print(best_sum(100, [1, 2, 5, 25], {}))
