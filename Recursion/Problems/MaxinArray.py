class Recursion:
    def MaxRecursion(self, int_list: list, cindex: int) -> int:
        if cindex == 0:
            return int_list[cindex]
        else:
             return max(int_list[cindex], Recursion.MaxRecursion(self, int_list, cindex-1))


Rec = Recursion()

sample_list = [1,2,4,6,8,9,3,2]

print("TheEasy Step" + str(max(sample_list)))

print(Rec.MaxRecursion(sample_list,len(sample_list)-1))
