

def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib(N - 1) + fib(N - 2)


cache = {0: 0, 1: 1}


def fib_mem(N, cache):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if cache[N] != 0:
        return cache[N]
    res = fib_mem(N - 1, cache) + fib_mem(N - 2, cache)
    cache[N] = res
    return res


def fib_dp(N):
    if N == 0: return 0
    if N == 1: return 1
    dp = [0 for _ in range(0, N + 1)]
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


def fib_dp_efficient(N):
    if N == 0: return 0
    if N == 1: return 1
    last_last = 0
    last = 1
    current = 0
    for i in range(2, N + 1):
        current = last + last_last
        last_last = last
        last = current
    return current


N = 10
cache = [0 for _ in range(0, N + 1)]
print(fib(N))

print(fib_mem(N, cache))

print(fib_dp(N))

print(fib_dp_efficient(N))
