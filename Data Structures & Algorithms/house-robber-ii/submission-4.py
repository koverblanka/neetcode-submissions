def rob_line(nums_line):
    rob1, rob2 = 0, 0

    for n in nums_line:
        curr = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = curr
    
    return rob2

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))