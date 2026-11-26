class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if target == curr_sum:
                return [left + 1, right + 1]
            elif target > curr_sum:
                left += 1
            else:
                right -= 1