class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Calculate distance for each point and push to a min-heap
        # Pop first k points
        # Return result array

        arr = list()
        result = list()

        for point in points:
            dist = ((point[0])**2 + (point[1])**2)**(0.5)
            arr.append((dist, point))
        
        heapq.heapify(arr)

        for _ in range(k):
            pnt = heapq.heappop(arr)
            result.append(pnt[1])
        
        return result


        