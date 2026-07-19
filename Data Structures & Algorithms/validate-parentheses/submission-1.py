class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if char == ')':
                    if (not stack) or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif char == ']':
                    if (not stack) or stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                else:
                    if (not stack) or stack[-1] != '{':
                        return False
                    else:
                        stack.pop()

        return not stack
