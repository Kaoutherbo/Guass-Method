import numpy as np
from back_substitution import back_substitution
from triangularization import triangularization

def  gaussian_elimination(matrix_A, vector_B):
    # Combine matrix A and vector B into an augmented matrix
    augmented_matrix = np.column_stack((matrix_A, vector_B))

    # Call the Gaussian elimination function
    modified_matrix, modified_vector = triangularization(augmented_matrix[:, :-1], augmented_matrix[:, -1])

    # Perform back-substitution
    solution_vector = back_substitution(modified_matrix, modified_vector)

    return solution_vector