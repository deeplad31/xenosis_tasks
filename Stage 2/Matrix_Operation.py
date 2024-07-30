import numpy as np

def get_matrix_input(matrix_number):
    rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
    cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))
    print(f"Enter the elements for Matrix {matrix_number} (row-wise): ")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            raise ValueError(f"Number of columns should be {cols}")
        matrix.append(row)
    return np.array(matrix)

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def display_matrix(matrix, matrix_name):
    print(f"{matrix_name}:\n{matrix}")

def main():
    print("Matrix Operations using Numpy")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice in [1, 2, 3]:
        matrix1 = get_matrix_input(1)
        matrix2 = get_matrix_input(2)
        
        display_matrix(matrix1, "Matrix 1")
        display_matrix(matrix2, "Matrix 2")
        
        if choice == 1:
            if matrix1.shape != matrix2.shape:
                print("Error: Matrices must have the same dimensions for addition.")
                return
            result = add_matrices(matrix1, matrix2)
            display_matrix(result, "Result (Addition)")
        
        elif choice == 2:
            if matrix1.shape != matrix2.shape:
                print("Error: Matrices must have the same dimensions for subtraction.")
                return
            result = subtract_matrices(matrix1, matrix2)
            display_matrix(result, "Result (Subtraction)")
        
        elif choice == 3:
            if matrix1.shape[1] != matrix2.shape[0]:
                print("Error: Number of columns in Matrix 1 must equal number of rows in Matrix 2 for multiplication.")
                return
            result = multiply_matrices(matrix1, matrix2)
            display_matrix(result, "Result (Multiplication)")
    
    elif choice == 4:
        matrix = get_matrix_input(1)
        display_matrix(matrix, "Matrix")
        result = transpose_matrix(matrix)
        display_matrix(result, "Result (Transpose)")
    
    else:
        print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
