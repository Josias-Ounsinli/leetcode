class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                j = nums[i+1:].index(diff) + (i+1)
                break
                
        return [i, j]