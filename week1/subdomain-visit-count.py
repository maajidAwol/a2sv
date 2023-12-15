class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        answer =[]
        numbers ={}
        for word in cpdomains:
            times = word.split(" ")
            sub_domain = times[1].split(".")
            subbed=sub_domain[len(sub_domain)-1]
            if subbed in numbers:
                    numbers[subbed]+=int(times[0])
            else:
                 numbers[subbed]=int(times[0])
            for i in range(len(sub_domain)-2,-1,-1):
                subbed = sub_domain[i] + "."+ subbed
                temp= times[0] + " " +subbed
                if subbed in numbers:
                    numbers[subbed]+=int(times[0])
                else:
                    numbers[subbed]=int(times[0])
        for key,value in numbers.items():
            new_temp = str(value) + " " +key
            answer.append(new_temp)
        return answer