class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Find all rotten fruits
        # Run multi source BFS on oranges
        # Count number of times bfs runs for max time, else -1

        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh_count = 0
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        while queue and fresh_count > 0:
            time += 1
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

        return time if fresh_count == 0 else -1



        