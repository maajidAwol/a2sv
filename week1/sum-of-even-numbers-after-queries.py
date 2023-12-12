class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([num for num in nums if num%2==0])
        answer =[0]*len(nums)
        for i in range(len(queries)):
            if nums[queries[i][1]] %2 ==0:
                even_sum =even_sum - nums[queries[i][1]]
            nums[queries[i][1]] +=queries[i][0]
            if nums[queries[i][1]] %2 ==0:
                even_sum =even_sum + nums[queries[i][1]]
            answer[i] = even_sum
        return answer
        