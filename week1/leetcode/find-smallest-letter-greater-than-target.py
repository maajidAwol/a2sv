class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # pos = bisect_right(letters,target)%len(letters)
        # return letters[pos]

        l = -1
        r = len(letters)
        while l+1 <r:
            mid = (l+r)//2
            
            if letters[mid] > target:
                r = mid
            elif letters[mid] <= target:
                l +=1
        pos = (l +1) % len(letters)
        return letters[pos]