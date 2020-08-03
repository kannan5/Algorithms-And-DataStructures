class Recursion:
    def PalindromeCheck(self, strVal, i, j):
        if i>j:
            return True
        return self.PalindromeCheck(strVal, i + 1, j - 1) if strVal[i] == strVal[j] else False


strVal = "q2eeeq"

obj = Recursion()

print(obj.PalindromeCheck(strVal, 0, len(strVal)-1))






