class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = max(nums)

        while l<=r:
            m = l + ((r-l) // 2)

            if nums[l] <= nums[m]:
                if nums[m] < res:
                    res = nums[l]
                l = m+1
            else:
                if nums[m] < res:
                    res = nums[m]
                r = m-1
            
        return res
