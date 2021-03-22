# Grid: m * n
# 
# Brute force:
# time : O()
# space: O()
#
# Memoized:
# time : O()
# space: O()

# m = 0 or n = 0 --> 0
# m = 1 or n = 1 --> 1
def grid_traveler(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if (n, m) in memo:
        return memo[(n, m)]
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    memo[(m, n)] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[(m, n)]


if __name__ == '__main__':
    print(grid_traveler(1, 1))
    print(grid_traveler(2, 3))
    print(grid_traveler(3, 2))
    print(grid_traveler(3, 3))
    print(grid_traveler(18, 18))
