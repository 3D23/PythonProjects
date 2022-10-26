class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        i_l = []
        helps = list(s)

        for i in range(len(s)):
            if (len(stack) == 0):
                i_l.append(i)
                stack.append(s[i])
            elif (s[i] == '('):
                stack.append(s[i])
            elif (s[i] == ')') and (len(stack) > 1):
                stack.pop()
            elif (s[i] == ')') and (len(stack) == 1):
                i_l.append(i)
                stack.pop()

        count = 0
        for i in i_l:
            helps.pop(i - count)
            count += 1

        answer = ''
        for i in helps:
            answer += i

        return answer

        # Алгоритм проходит по всем элементам s, находит индексы открывающих и закрывающих главных скобок. В лист helps записывает все элементы s корме главных открывающих и закрывающих скобок. В строку answer записываются все элементы листа helps.
        # Сложность O(len(s))