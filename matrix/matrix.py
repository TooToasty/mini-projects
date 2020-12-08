class Matrix:
    def __init__(self, matrix_string):
        self.string = matrix_string

    def row(self, index):
        split_matrix = self.string.split("\n")
        return list(map(int, split_matrix[index - 1].split()))

    def column(self, index):
        result = []
        split_matrix = self.string.split("\n")
        matrix_col_len = len(split_matrix)
        idx = 0
        while idx != matrix_col_len:
            current_line = split_matrix[idx].split()
            result.append(int(current_line[index - 1]))
            idx += 1
        return result
