class RecursionOps:
    @staticmethod
    def recursion(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return n * RecursionOps.recursion(n-1)




print(RecursionOps.recursion(5))