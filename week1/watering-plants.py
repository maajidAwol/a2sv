class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        fill = capacity
        steps=0
        for i in range(len(plants)):

            if fill>= plants[i]:
                steps+=1
            else:
                fill= capacity   
                steps +=((i*2)+1)
            fill -= plants[i]
        return steps