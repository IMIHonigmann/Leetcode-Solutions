class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lastFoundMatch = -1

        while l<=r:
            m = ((r-l) // 2) + l
            hoursNeeded = 0

            for pile in piles:
                hoursNeeded += math.ceil(pile / m)

            if hoursNeeded <= h:
                lastFoundMatch = m
                r=m-1
            elif hoursNeeded > h:
                l=m+1

        return lastFoundMatch
