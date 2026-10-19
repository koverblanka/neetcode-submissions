class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_minus_ith = []

        for i in range(len(nums)):
            target_minus_ith.append(target - nums[i])
        print(target_minus_ith)

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] in target_minus_ith:
                return [target_minus_ith.index(nums[j]), j]