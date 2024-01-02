class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
      processorTime.sort()
      tasks.sort(reverse =True)
      step = 0
      n = len(processorTime)
      for i in range(n):    
          for j in range(4):
              tasks[step] += processorTime[i]
              step +=1
      return max(tasks)