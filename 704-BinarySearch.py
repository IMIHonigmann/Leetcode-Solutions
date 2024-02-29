class Solution:
    def search(self, nums: List[int], target: int) -> int:
        goToIndex = 0
        
        while True:
            slicedLength = len(nums) // 2
            
            if nums[slicedLength] < target:
                goToIndex += slicedLength
                nums = nums[slicedLength:]
            elif nums[slicedLength] > target:
                nums = nums[:slicedLength]
            elif nums[slicedLength] == target:
                goToIndex += slicedLength
                return goToIndex

            if slicedLength == 0:
                return -1

        return -1