# m = target
# n = size(nums)
#
# Brute force:
# time : O()
# space: O()
#
# Memoized:
# time : O()
# space: O()


def can_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        rem = target - num
        if can_sum(rem, nums, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


if __name__ == '__main__':
    print(can_sum(7, [2, 3], {}))
    print(can_sum(7, [5, 3, 4, 7], {}))
    print(can_sum(7, [2, 4], {}))
    print(can_sum(7, [2, 3, 5], {}))
    print(can_sum(300, [7, 14], {}))
