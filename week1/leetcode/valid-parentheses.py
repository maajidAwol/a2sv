class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:

            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif stack:
                if stack[-1] == "(" and ch == ")":
                    stack = stack[:-1]
                elif stack[-1] == "{" and ch == "}":  
                    stack = stack[:-1]
                elif stack[-1] == "[" and ch == "]":
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False
    
        if not stack:
            return True