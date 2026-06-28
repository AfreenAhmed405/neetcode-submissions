class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # Find all unsafe O on the edges
        # Start BFS from the unsafe O and change all connected O to Y
        # Convert all O to X and Y to O

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    board[r][c] = "#"
                    self.bfs(r, c, board)

        print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
    
    def bfs(self, r: int, c: int, board: List[List[str]]) -> None:
        queue = deque([(r, c)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) - 1 and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))   


