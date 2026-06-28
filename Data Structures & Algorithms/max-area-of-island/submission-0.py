class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.bfs(r, c, grid))

        return max_area
        
    
    def bfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        grid[r][c] = 0
        queue = deque([(r, c)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 1

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    count += 1
        
        return count

                

