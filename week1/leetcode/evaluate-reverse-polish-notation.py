class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+","/","-","*"}
        for tok in tokens:
            if tok in op:
                val2 = stack.pop()
                val1 = stack.pop()
                if tok == "+":
                    stack.append(val1+val2)
                elif tok == "-":
                    stack.append(val1-val2)
                elif tok == "*":
                    stack.append(val1*val2)
                elif tok == "/":
                    if val1/val2 < 0:
                        stack.append(math.ceil(val1/val2))
                    else:
                        stack.append(val1//val2)
            else:
                stack.append(int(tok))
        return stack[0]

