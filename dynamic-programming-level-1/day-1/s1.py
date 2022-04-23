def fib(N):
    if N == 0:
        return 0
    memo = [0, 1]
    for _ in range(2, N+1):
        memo = [memo[-1], memo[-1] + memo[-2]]

    return memo[-1]


# def fib(self, N):
#     golden_ratio = (1 + 5 ** 0.5) / 2
#     return int((golden_ratio ** N + 1) / 5 ** 0.5)
