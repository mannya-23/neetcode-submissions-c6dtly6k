class Solution:
    def isValid(self, s: str) -> bool:
        par = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in par:
                if stack and stack[-1] == par[char]:
                    stack.pop()
                else:
                    return False
            else:
                 stack.append(char)
        return True if len(stack) == 0 else False