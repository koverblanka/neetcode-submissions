class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = set()

        for x in nums:
            if x in has_seen:
                return True
            else:
                has_seen.add(x)
        return False
        