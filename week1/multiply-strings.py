class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1=0
        int_num2=0
        for i in range(len(num1)):
            int_num1*=10
            int_num1 +=ord(num1[i])-48
        for i in range(len(num2)):
            int_num2*=10
            int_num2 +=ord(num2[i])-48
        return str(int_num1*int_num2)