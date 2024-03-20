class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr,right_arr):
            i=0
            j=0
            mer = []
            while i <len(left_arr) and j<len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    mer.append(left_arr[i])
                    i+=1
                else:
                    mer.append(right_arr[j])
                    j+=1
            mer.extend(left_arr[i:])
            mer.extend(right_arr[j:])
            return mer
        def mergeSort(left,right):
            if left == right:
                return [nums[left]]
            mid = (left +right)//2
            left_arr = mergeSort(left,mid)
            right_arr = mergeSort(mid+1,right)
            return merge(left_arr,right_arr)
        return mergeSort(0,len(nums)-1)