class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    sum_ =0
                    while stack[-1] != "(":
                        sum_ += stack.pop()
                    stack.pop()
                    stack.append(sum_ *2)
    
        return sum(stack)