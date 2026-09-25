class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        sett = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in sett:
                return [sett[compliment], i]
            else:
                sett[nums[i]] = i

