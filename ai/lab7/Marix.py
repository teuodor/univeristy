def _determinant_matrix(matrix):
    to_return = 0
    if len(matrix) == 2:
        to_return = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(len(matrix)):
            to_return += ((-1) ** i) * matrix[0][i] * _determinant_matrix(_minor_matrix(matrix, 0, i))

    return to_return


def _minor_matrix(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def _transposed_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transposed(self):
        return _transposed_matrix(self.matrix)

    def multiplication(self, other):
        return [[sum(a*b for a, b in zip(self_row, other_col)) for other_col in zip(*other.matrix)] for self_row in self.matrix]

    def determinant(self):
        return _determinant_matrix(self.matrix)

    def minor(self, i , j):
        return _minor_matrix(self.matrix, i, j)

    def reverse(self):
        determinant = self.determinant()
        if len(self.matrix) == 2:
            return [[self.matrix[1][1] / determinant, -1 * self.matrix[0][1] / determinant],
                    [-1 * self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]]

        adjacent_matrix = []
        for i in range(len(self.matrix)):
            current_line = []
            for j in range(len(self.matrix)):
                minor = self.minor(i, j)
                current_line.append(((-1)**(i+j)) * _determinant_matrix(minor))
            adjacent_matrix.append(current_line)

        adjacent_matrix = _transposed_matrix(adjacent_matrix)

        for i in range(len(adjacent_matrix)):
            for j in range(len(adjacent_matrix)):
                adjacent_matrix[i][j] = adjacent_matrix[i][j] / determinant

        return adjacent_matrix
