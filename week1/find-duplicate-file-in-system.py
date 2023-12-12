class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content= {}
       
        # s="1.txt(abcd)"
        # s=s.split("(")
        # s =s[1].split(")")
        # print(s)
        answer =[]
        for path in paths:
            temp = path.split()
            directory  =temp[0]
            for i in range(1,len(temp)):
                string = temp[i].split("(")
                key =string[1].split(")")
                key =key[0]
                if key in content:
                    content[key].append(directory + "/"+string[0])
                else:
                    content[key] =[]
                    content[key].append(directory + "/"+string[0])
        for value in content.values():
            if len(value) >=2:
                answer.append(value)
        return answer