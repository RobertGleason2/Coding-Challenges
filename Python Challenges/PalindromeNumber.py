class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            tmpval = 0
            if x%10 == 0 and x != 0:
                return False
            while x > tmpval:
                tmpval = tmpval * 10 + x%10
                x = x // 10
            return x == tmpval or x == tmpval//10
        else:
            return False