class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = ''
        while (n > 0):
            s += str(n % k)
            n = n // k
        summ = 0
        for i in s:
            summ += int(i)
        return summ

    # Алгоритм переводит число n в десятичной системе счисления в степень счисления k, потом ввыводит сумму цифр числа n в степени счисления k.
    # Сложность - O(logk(n))