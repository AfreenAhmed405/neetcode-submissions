class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        print(rows, cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(r, c, grid)
        return count
    
    def bfs(self, r: int, c: int, grid: List[List[str]]):
        grid[r][c] == "0"
        queue = deque([(r, c)])
        print(queue)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"