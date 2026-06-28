class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Calculate distance for each point and push to a min-heap
        # Pop first k points
        # Return result array

        max_heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(max_heap, (-dist, point))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [point for dist, point in max_heap]        