'''
no.of rows represents = i
row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] -> i-1 => previous row
'''

def generate(numRows):
    triangle = []  # Final result list

    for i in range(numRows):
        row = [1] * (i + 1)  # Start each row with all 1s

        # Update the values in the middle (not the first or last)
        for j in range(1, i):
            # Sum of two numbers above it: triangle[i-1][j-1] + triangle[i-1][j]
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the completed row to the triangle

    return triangle

print(generate(5))