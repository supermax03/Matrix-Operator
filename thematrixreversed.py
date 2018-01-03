import sys


class TheMatrixReversed:

    @classmethod
    def revert(cls, input_matrix=[[]]):
        result = []
        try:
            dim = len(input_matrix[0])
            for i_index in range(dim):
                row = []
                for j_index in range(len(input_matrix)):
                    row.append(input_matrix[j_index][i_index])
                result.append(row)
        except:
            print sys.exc_info()
        finally:
            return result

    def __init__(self):
        pass


if __name__ == '__main__':
    matrix = [[1, 5, 6], [8, 9, 7], [6, 7, 8], [9, 5, 7]]
    print TheMatrixReversed.revert(matrix)
