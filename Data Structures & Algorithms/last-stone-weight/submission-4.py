import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y, x = heapq.nsmallest(2, stones)
            print(-y,-x)

            if x == y:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:  # x > y, both negative, 
                heapq.heappop(stones) # pop y
                heapq.heapreplace(stones, y - x) # replace x by y - x
        
        return - stones[0] if len(stones) > 0 else 0
