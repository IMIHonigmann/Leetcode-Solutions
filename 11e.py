class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        # bfe = BiggestFoundElement
        bfe = 0
        lowerElement = -1

        for i in range(len(height)):
            distance = r-l
            if height[l] < height[r]:
                lowerElement = height[l]
                l+=1
            else:
                lowerElement = height[r]
                r-=1
            
            if bfe < lowerElement * distance:
                bfe = lowerElement * distance
            
            if l == r:
                return bfe

        return bfe