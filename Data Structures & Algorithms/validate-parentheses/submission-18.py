class Solution:
    def isValid(self, s: str) -> bool:
        par = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if stack and char in par:
                if stack[-1] == par[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        return False