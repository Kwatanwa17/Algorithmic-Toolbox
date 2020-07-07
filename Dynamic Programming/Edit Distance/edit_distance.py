# python3


def edit_distance(first_string, second_string):
    # create an initial matrix (size = len(first_string) + 1 by len(second_string) + 1)_
    mat = []

    # first row
    mat.append(list(range(len(second_string) + 1)))

    # fill the matrix
    for row in range(1, (len(first_string) + 1)):
        row_vec = [row] + [0] * len(second_string)
        mat.append(row_vec)

    # compute edit distance
    for col_idx, col in enumerate(second_string, 1):
        for row_idx, row in enumerate(first_string, 1):
            insertion = mat[row_idx][col_idx - 1] + 1
            deletion = mat[row_idx - 1][col_idx] + 1

            if col == row:
                match = mat[row_idx - 1][col_idx - 1]
                dist = min(insertion, deletion, match)
                mat[row_idx][col_idx] = dist
            else:
                mismatch = mat[row_idx - 1][col_idx - 1] + 1
                dist = min(insertion, deletion, mismatch)
                mat[row_idx][col_idx] = dist

    # return the last element
    return mat[-1][-1]





if __name__ == "__main__":
    print(edit_distance(input(), input()))
