class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(right + left)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(token))
        return int(stack[-1])

            