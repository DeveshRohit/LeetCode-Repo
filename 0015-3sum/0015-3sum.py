class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        for target in range(len(nums)):
            i = target + 1
            j = len(nums) - 1
            if target != 0 and nums[target] == nums[target - 1]:
                continue
            while i<j:
                lesser_target = 0 - nums[target]
                if nums[i] + nums[j] > lesser_target:
                    j -= 1
                elif nums[i] + nums[j] < lesser_target:
                    i += 1
                else:
                    res.append([nums[i], nums[j], nums[target]])
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                    j -= 1

        return res