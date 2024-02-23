class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        # print(path)
    
        for ch in path:
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch != "" and ch !=".":
                
                stack.append(ch)
            
        # print(stack)
        
        return "/" +"/".join(stack)