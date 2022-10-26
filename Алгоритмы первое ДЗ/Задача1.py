class Solution:
    def numberOfSteps(self, num: int) -> int:

        def rec(num):
            if (num == 1):
                return 1
            elif (num > 1) and (num % 2 == 0):
                return rec(num // 2) + 1
            elif (num > 1) and (num % 2 != 0):
                return rec(num - 1) + 1

        if (num == 0):
            return 0
        else:
            return rec(num)

    # Алгоритм проходит по рекурсивной функции и добавляет 1 к возвращению функции, пока num не будет 1.
    # Сложность - приблизительно O(log(num))
