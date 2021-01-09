from matrix import Matrix
import time
from random import randint
import numpy as np


if __name__ == '__main__':
    first_matrix = [[randint(1, 10) for _ in range(5)] for _ in range(5)]
    second_matrix = [[randint(1, 10) for _ in range(5)] for _ in range(5)]

    first_matrix_c = Matrix(first_matrix)
    second_matrix_c = Matrix(second_matrix)
    start = time.time()
    c_answer = first_matrix_c.mult_matrix(second_matrix_c)
    result_c = time.time() - start

    first_np_matrix = np.array(first_matrix)
    second_np_matrix = np.array(second_matrix)

    start = time.time()
    np_answer = first_np_matrix @ second_np_matrix
    result_np = time.time() - start
    if result_c < result_np:
        print(f'C marix:{result_c}')
        print(f'NP marix:{result_np}')
        print(f'C Matrix is faster than NP {round(result_c/result_np, 1)} times more')
    else:
        print(f'C marix:{result_c}')
        print(f'NP marix:{result_np}')
        print(f'NP Matrix is faster than NP {round(result_c/result_np, 1)} times more')
