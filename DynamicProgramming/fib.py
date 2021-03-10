memo = {1: 0, 2: 1}


class Fib:

    def fib(self, val):
        if val == 1:
            return 0
        if val == 2:
            return 1
        return self.fib(val - 1) + self.fib(val - 2)

    def fib_memo(self, val, memo_cache):
        if val in memo_cache:
            return memo_cache[val]
        else:
            memo_cache[val] = self.fib_memo(val - 1, memo_cache) + self.fib_memo(val - 2, memo_cache)
            return memo_cache[val]


if __name__ == '__main__':
    a = Fib()
    print(a.fib_memo(9, memo))
