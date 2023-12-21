class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in range(len(digits)):
            num +=str(digits[i])
        num = int(num) +1
        num = str(num)
        num_list = [0] *len(num)
        for i in range(len(num)):
            num_list[i] = int(num[i])
        return num_list