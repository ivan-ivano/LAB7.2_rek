import random


def find_max_element(array, a, index=0, max_el=None):
    if index == len(array):
        if max_el is not None:
            a.append(max_el)
        return
    if max_el is None or array[index] > max_el:
        max_el = array[index]
    find_max_element(array, a, index + 1, max_el)


def find_min_element(array, index=0, min_el=None):
    if index == len(array):
        return min_el
    if min_el is None or array[index] < min_el:
        min_el = array[index]
    return find_min_element(array, index + 1, min_el)


def processing_matrix(matrix, a, row_index=0):
    if row_index == len(matrix):
        return
    find_max_element(matrix[row_index], a, 0, None)
    processing_matrix(matrix, a, row_index + 1)


def create_matrix(rows, cols, lower_limit, upper_limit, current_row=0, matrix=None):
    if matrix is None:
        matrix = []

    if current_row == rows:
        return matrix

    if len(matrix) <= current_row:
        matrix.append([])

    matrix[current_row].append(random.randint(lower_limit, upper_limit))

    if len(matrix[current_row]) == cols:
        return create_matrix(rows, cols, lower_limit, upper_limit, current_row + 1, matrix)

    return create_matrix(rows, cols, lower_limit, upper_limit, current_row, matrix)


def print_matrix(matrix, index=0, row=0):
    if row >= len(matrix):
        return

    if index < len(matrix[row]):
        print(f"{matrix[row][index]:>5}{'  ' if index == len(matrix[row]) - 1 else ''}", end='')
        return print_matrix(matrix, index + 1, row)
    elif index == len(matrix[row]):
        print()
        return print_matrix(matrix, 0, row + 1)


if __name__ == '__main__':
    max_list = []
    rowss, colss = 8, 6
    low_limit, high_limit = 16, 97
    R = create_matrix(rowss, colss, low_limit, high_limit)
    print_matrix(R)
    processing_matrix(R, max_list)
    print("Найменший з максимальних елементів по всіх рядках матриці:", find_min_element(max_list))
