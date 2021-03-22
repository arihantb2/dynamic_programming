# m = target
# n = size(nums)
#
# Brute force:
# time: O(n^m * m) (tree span * copying array and returning)
# space: O(m) (tree span)
#
# Memoized:
# time: O(n * m * m) (memoized tree span * copying array and returning)
# space: O(m * m) (holding memoized array for each possible target, worst case : m keys in memo)


def how_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        rem = target - num
        result = how_sum(rem, nums, memo)
        if result is not None:
            memo[target] = result + [num]
            return memo[target]

    memo[target] = None
    return None


if __name__ == '__main__':
    print(how_sum(7, [2, 3], {}))
    print(how_sum(7, [5, 3, 4, 7], {}))
    print(how_sum(7, [2, 4], {}))
    print(how_sum(8, [2, 3, 5], {}))
    print(how_sum(300, [7, 14], {}))
    print(how_sum(300, [14, 16], {}))
