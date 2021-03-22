# n = fibonacci series index
#
# Brute force:
# time : O()
# space: O()
#
# Memoized:
# time : O()
# space: O()

def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
