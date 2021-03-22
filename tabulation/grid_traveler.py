import numpy as np

# m = number of rows
# n = number of cols
# Time : O(m * n)
# Space: O(m * n)


def grid_treveler(m, n):
    table = np.zeros((m + 1, n + 1), dtype=int)
    table[1, 1] = 1

    for i in range(0, m+1):
        for j in range(0, n+1):
            curr = table[i, j]
            if i + 1 <= m:
                table[i + 1, j] = table[i + 1, j] + curr
            if j + 1 <= n:
                table[i, j + 1] = table[i, j + 1] + curr

    return table[m, n]


if __name__ == '__main__':
    print(grid_treveler(1, 1))
    print(grid_treveler(2, 3))
    print(grid_treveler(3, 2))
    print(grid_treveler(3, 3))
    print(grid_treveler(18, 18))