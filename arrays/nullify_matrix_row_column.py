import numpy as np


# ------- Nullify matrix row/column if the row/column has a zero. ------- #

def nullify_matrix_row_column(m, num_rows, num_columns):
    first_row_has_zero = False
    first_col_has_zero = False

    for column in range(1, num_columns):
        if m[0][column] == 0:
            first_row_has_zero = True
            break

    for row in range(1, num_rows):
        if m[row][0] == 0:
            first_col_has_zero = True
            break

    # Check remaining rows/columns and mark first row and column element as 0 if there is any 0 in that column/row
    for row in range(1, num_rows):
        for column in range(1, num_columns):
            if m[row][column] == 0:
                m[0][column] = 0  # set first row element in that column to 0
                m[row][0] = 0  # set first column element in that row to 0

    # now nullify each column if first row is zero
    for col in range(1, num_columns):
        if m[0][col] == 0:
            for row in range(1, num_rows):
                m[row][col] = 0

    # And nullify each row if first col is zero
    for row in range(1, num_rows):
        if m[row][0] == 0:
            for col in range(1, num_columns):
                m[row][col] = 0

    # finally set first row/column zero if required
    if first_row_has_zero:
        for column in range(num_columns):
            m[0][column] = 0
    if first_col_has_zero:
        for row in range(num_rows):
            m[row][0] = 0

    return m


input_matrix = [[11, 18, 0, 5],
                [9, 15, 6, 8],
                [0, 6, 2, 6],
                [1, 4, 5, 14]]

output_matrix = nullify_matrix_row_column(input_matrix, 4, 4)
print(np.array(output_matrix))
