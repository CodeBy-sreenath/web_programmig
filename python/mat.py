def max_sum_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    # Fix left column
    for left in range(cols):
        temp = [0] * rows
        
        # Fix right column
        for right in range(left, cols):
            
            # Add current column values to temp
            for row in range(rows):
                temp[row] += matrix[row][right]
            
            # Apply Kadane’s Algorithm on temp
            curr_sum = temp[0]
            best_sum = temp[0]
            for i in range(1, rows):
                curr_sum = max(temp[i], curr_sum + temp[i])
                best_sum = max(best_sum, curr_sum)
            
            max_sum = max(max_sum, best_sum)
    
    return max_sum
