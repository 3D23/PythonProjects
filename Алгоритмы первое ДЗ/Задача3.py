class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count

    # Алгоритм проходит по циклу len(stones) количество раз. Если в jewels есть элемент stones, то count увеличивается на 1
    # Сложность - O(len(stones))