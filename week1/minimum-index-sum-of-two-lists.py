class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sums={}
        ans =[]
        for string in list1:
            if string in list2:
              if list1.index(string) + list2.index(string) in sums:
                sums[list1.index(string) + list2.index(string)].append(list1.index(string))
              else:
                sums[list1.index(string) + list2.index(string)] =[]
                sums[list1.index(string) + list2.index(string)].append(list1.index(string))
        new_sums =list(sums.keys())
        new_sums.sort()
        ans_list = sums[new_sums[0]]
        for add in ans_list:
          ans.append(list1[add])

        return ans