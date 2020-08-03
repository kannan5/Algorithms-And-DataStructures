class Recursion:
    def SequenceCheck(self, int_val: int, last_el: int = 0) -> bool:
        if last_el == 0:
            last_el = int_val % 10
        int_val = int_val // 10
        res_el = int_val % 10
        if int_val == last_el-1:
            return True
        if last_el - res_el == 1 or last_el - res_el == 0:
              res = self.SequenceCheck(int_val, last_el-1)
        else:
            res = False
        return res

    # def SequenceCheck2(self, int_val: int, last_el: int = 0) -> bool:
    #     return self.SequenceCheck(int_val, last_el-1)


obj = Recursion()

print(obj.SequenceCheck(123456))



