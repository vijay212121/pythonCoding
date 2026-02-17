def set_zeroes(matrix):
    # Step 1: Get matrix dimensions
    m, n = len(matrix), len(matrix[0])

    # Step 2: Check if the first row has any zero
    # We need to handle the first row separately because we'll use it later as a flag area
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))

    # Step 3: Check if the first column has any zero
    # Same reason as above — to remember if first column needs to be zeroed in the end
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Step 4: Use the rest of the matrix (excluding first row & column) to mark rows & columns
    # If matrix[i][j] == 0 → mark its row and column by setting matrix[i][0] and matrix[0][j] to 0
    # here, if u find any element is zero in inner matrix, then make it's first ro element and first column element to zero.
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row
                matrix[0][j] = 0  # Mark the column

    # Step 5: traverse through the inner matrix, if u find either it's row or column to zero, then set that element to 0
    # Set matrix[i][j] = 0 if its row or column is marked (based on first row/col)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 6: After processing inner matrix, handle the first row if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0  # Set entire first row to zero

    # Step 7: After processing inner matrix, handle the first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0  # Set entire first column to zero


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 0, 5]]
set_zeroes(matrix)
print(matrix)
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

