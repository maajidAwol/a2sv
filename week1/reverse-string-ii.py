class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        total = len(s)
        ptr = 0
        while ptr < total:
            result += s[ptr:ptr+k][::-1]
            ptr += k
            result += s[ptr:ptr+k]
            ptr += k

        return result
