class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        target_row = -1

        while up <= down:
            mid_row = (up + down) // 2
            
            # Check if target is within the bounds of this row
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            elif matrix[mid_row][0] < target:
                up = mid_row + 1
            else:
                down = mid_row - 1
                
        # If no valid row could contain the target
        if target_row == -1:
            return False

        while left <= right:
            mid_col = (left + right) // 2
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1 

        return False






        