import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-num for num in gifts]

        # min-heap for negated values, i.e., max-heap for values
        heapq.heapify(heap)

        for _ in range(k):
            max_value = - heap[0]
            heapq.heapreplace(heap, - math.floor(sqrt(max_value)))

        return sum([-x for x in heap])

        
