class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Find all the sources (0)
        # Add all sources to a queue
        # Run a multi source BFS updating INF to distance

        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_value = 2147483647
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            dist += 1
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == max_value:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))