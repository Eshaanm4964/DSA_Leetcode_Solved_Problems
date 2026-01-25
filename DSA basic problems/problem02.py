def reverseNumber(self, n):
        reverse_Num = 0
        while n > 0:
            lastDigit = n % 10
            reverse_Num = reverse_Num * 10 + lastDigit
            n = n // 10
        return reverse_Num