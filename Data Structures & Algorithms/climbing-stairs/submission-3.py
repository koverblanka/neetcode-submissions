class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        second_to_last = 1
        last = 2
        for i in range(3, n+1):
            curr = last + second_to_last
            second_to_last = last
            last = curr
        return curr
        