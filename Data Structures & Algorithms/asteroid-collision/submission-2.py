class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0: 
                # check asteroid against next ast in stack since its bigger
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    continue
                # same size, both destroyed
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                # smaller, immediately destroyed 
                else:
                    break
            else:
                stack.append(ast)
        return stack
            

