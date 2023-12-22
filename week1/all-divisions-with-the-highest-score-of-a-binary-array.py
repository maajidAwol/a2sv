class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # count = defaultdict(list)
        # sum_1 = [0] * len(nums) 
        # sum_0 = [0] * len(nums)
        # sum_zero = 0
        # sum_one = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         sum_zero +=1
        #         sum_0[i] = sum_zero
        #     if nums[i] == 1:
        #         sum_one +=1
        #         sum_1[i] = sum_one
        # print(sum_1)
        # print(sum_0)
             


        # for i in range(len(nums)+1):
        #     left = nums[:i].
        #     right = nums[i:].count(1)
        #     count[left+right].append(i)
        # return count[max(count)]
        n = len(nums)
        one = nums.count(1)
        zero = nums.count(0)
        zeros =0
        ones = nums.count(1)
        count = defaultdict(list)
        count[one].append(0)
        count[zero].append(n)
        idx = 0
        for i in range(1,len(nums)):        
            if nums[idx]==0:
               zeros +=1
            elif nums[idx] ==1:
                
                ones -=1
            count[zeros + ones].append(i)
            idx +=1
        return count[max(count)]