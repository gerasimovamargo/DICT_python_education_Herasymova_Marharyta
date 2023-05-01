"""WORKING WITH MATRICES"""

# Libraries
import random
import sys


def show_one_matrix() -> list[list[int]]:
    """
    the function asks for the number of rows and the number of rows for the matrix,
    and then outputs a column of a randomly generated matrix with a description.

        Returns:
        -------
               matrix1 (list[list[int]]): A randomly generated matrix as a list of lists of integers.
    """
    while True:
        try:
            num_rows1 = int(input("Enter the number of rows: "))
            num_cols1 = int(input("Enter the number of columns: "))
            if num_rows1 <= 0 or num_cols1 <= 0:
                raise ValueError("Number of rows and columns must be positive integers.")
        except ValueError:
            print("invalid literal for int()")
            continue
        matrix1 = []
        for i in range(num_rows1):
            row = []
            for j in range(num_cols1):
                row.append(random.randint(1, 10))
            matrix1.append(row)

        print("Matrix 1:")
        for row in matrix1:
            print(row)
        return matrix1


def show_two_matrix() -> tuple[list[list[int]], list[list[int]]]:
    """
    the function asks the user for the number of rows and columns for two matrices
    and then outputs two randomly generated matrices with the specified size.

       Returns:
       -------
              matrix1 (list[list[int]]): Randomly generated matrix 1 as a list of lists of integers.
              matrix2 (list[list[int]]): Randomly generated matrix 2 as a list of lists of integers.
    """
    while True:
        try:
            num_rows1 = int(input("Enter the number of rows for the first matrix: "))
            if num_rows1 <= 0:
                raise ValueError
            num_cols1 = int(input("Enter the number of columns for the first matrix: "))
            if num_cols1 <= 0:
                raise ValueError
            num_rows2 = int(input("Enter the number of rows for the second matrix: "))
            if num_rows2 <= 0:
                raise ValueError
            num_cols2 = int(input("Enter the number of columns for the second matrix: "))
            if num_cols2 <= 0:
                raise ValueError
        except ValueError:
            print('Wrong input. Enter a positive integer!')
            continue

        if num_cols1 != num_rows2:
            print("Error: The number of columns of the first matrix must be equal to the number of rows "
                  "of the second matrix.")
            continue

        matrix1 = []
        for i in range(num_rows1):
            row = []
            for j in range(num_cols1):
                row.append(random.randint(1, 10))
            matrix1.append(row)

        matrix2 = []
        for i in range(num_rows2):
            row = []
            for j in range(num_cols2):
                row.append(random.randint(1, 10))
            matrix2.append(row)

        print("Matrix 1:")
        for row in matrix1:
            print(row)

        print("Matrix 2:")
        for row in matrix2:
            print(row)

        return matrix1, matrix2


def addition_of_two_matrices() -> None:
    """the function runs the show_two_matrix() function to get the two matrices to add.
    Then the dimensions of the matrices are checked, if they are not equal, then an error message is displayed.
    Otherwise, the matrices are added and the result is displayed on the screen."""
    while True:
        matrix1, matrix2 = show_two_matrix()
        num_rows1 = len(matrix1)
        num_rows2 = len(matrix2)
        num_cols1 = len(matrix1[0])
        num_cols2 = len(matrix2[0])
        if num_rows1 != num_rows2 or num_cols1 != num_cols2:
            print("Error: The two matrices must have the same size!")
            continue
        elif matrix1 is None or matrix2 is None:
            return
        else:
            result = []
            for i in range(num_rows1):
                row = []
                for j in range(num_cols1):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result.append(row)

            print("Result:")
            for row in result:
                print(row)
            break


def multiply_by_constant() -> None:
    """the function runs the show_one_matrix() function to get the matrix to multiply by the number.
    The user is then asked for a number to multiply.
    If the entered value is not a number, an error message is displayed. Otherwise,
    the matrix is multiplied by the number and the result is displayed on the screen."""
    matrix1 = show_one_matrix()
    while True:
        matrix_const = input("Enter constant -> ")
        try:
            float(matrix_const)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        result = [[matrix1[i][j] * float(matrix_const) for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        print("RESULT")
        for r in result:
            print(r)
        break


def multiply_matrices() -> None:
    """the function runs the show_two_matrix() function to get the two matrices to multiply.
    Then the matrix sizes are checked, if they do not meet the requirements for matrix multiplication,
    an error message is displayed. Otherwise, the matrix is multiplied and the result is displayed on the screen."""
    while True:
        matrix1, matrix2 = show_two_matrix()
        num_rows2 = len(matrix2)
        num_cols1 = len(matrix1[0])
        num_cols2 = len(matrix2[0])
        if matrix1 is None or matrix2 is None:
            return
        if num_cols1 != num_rows2:
            print("Error: The number of columns of the first matrix must be equal to the number of rows "
                  "of the second matrix.")
            continue
        result = [[0 for _ in range(num_cols2)] for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(num_cols2):
                for k in range(num_cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print("Result:")
        for row in result:
            print(row)
        break


def transpose_matrix() -> None:
    """
    The function runs the show_one_matrix() function to get the matrix to be transposed.
    Then the matrix is transposed using the specified method and the result is displayed on the screen.

    """
    matrix1 = show_one_matrix()
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])

    while True:
        print("Choose a transpose method:")
        print("1. Standard")
        print("2. Main diagonal")
        print("3. Vertical axis")
        print("4. Horizontal axis")
        choice = input("Enter your choice: ")

        if choice == "1":
            transposed = [[matrix1[j][i] for j in range(num_rows)] for i in range(num_cols)]
            transpose_method = "standard"
            break
        elif choice == "2":
            transposed = [[matrix1[j][i] for j, i in zip(range(num_rows), range(num_cols))] for _ in range(num_cols)]
            transpose_method = "main diagonal"
            break
        elif choice == "3":
            transposed = [row[::-1] for row in matrix1]
            transpose_method = "vertical axis"
            break
        elif choice == "4":
            transposed = matrix1[::-1]
            transpose_method = "horizontal axis"
            break
        else:
            print("Invalid choice")

    print(f"{transpose_method.capitalize()} transposed matrix:")
    for row in transposed:
        print(row)


def show_determinant() -> None:
    """The function calls the determinant function to calculate the determinant of the matrix
    and prints the result on the screen.
    """
    det = determinant()
    print(f"The determinant is: {det}")


def determinant(matrix1=None) -> int:
    """
    the function runs the show_one_matrix() function to get the matrix whose determinant is to be found.
    Then the determinant of the matrix is determined (if the matrix is 1x1 or 2x2,
    then the determinant is found by the formula, otherwise recursion is used).
    The result is displayed on the screen.

        Parameters:
        -----------
            matrix1: list[list[int]], optional
                The matrix to calculate the determinant of. If not provided, the user is prompted to enter a matrix.

        Returns:
        --------
            det: int
                The determinant of the matrix.
    """
    if matrix1 is None:
        matrix1 = show_one_matrix()
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])
    if num_rows == 1 and num_cols == 1:
        det = matrix1[0][0]
    elif num_rows == 2 and num_cols == 2:
        det = matrix1[0][0] * matrix1[1][1] - matrix1[0][1] * matrix1[1][0]
    else:
        det = 0
        for i in range(num_cols):
            sign = (-1) ** i
            sub_matrix = []
            for j in range(1, num_rows):
                row = []
                for k in range(num_cols):
                    if k != i:
                        row.append(matrix1[j][k])
                sub_matrix.append(row)
            det += sign * matrix1[0][i] * determinant(sub_matrix)
    return det


def inverse_matrix() -> None:
    """the function runs the show_one_matrix() function to get the matrix whose inverse is to be found.
    Then there is a check whether the matrix is square.
    If not, an error message is displayed.
    Otherwise, the inverse matrix is searched and the result is displayed on the screen."""
    matrix1 = show_one_matrix()
    # check if the matrix is square
    if len(matrix1) != len(matrix1[0]):
        print("Error: Matrix is not square.")
        return None
    # create an identity matrix
    identity = []
    for i in range(len(matrix1)):
        row = [0] * len(matrix1)
        row[i] = 1
        identity.append(row)
    # perform row operations to transform the matrix into the identity matrix
    for i in range(len(matrix1)):
        pivot = matrix1[i][i]
        if pivot == 0:
            print("Error: Matrix is not invertible.")
            return None
        for j in range(len(matrix1)):
            matrix1[i][j] /= pivot
            identity[i][j] /= pivot
        for k in range(len(matrix1)):
            if k == i:
                continue
            factor = matrix1[k][i]
            for j in range(len(matrix1)):
                matrix1[k][j] -= factor * matrix1[i][j]
                identity[k][j] -= factor * identity[i][j]
    # the identity matrix has been transformed into the inverse of the original matrix
    inverse = identity
    print("Inverse Matrix:")
    for row in inverse:
        print(row)


def menu():
    """А function that has an application menu"""
    print('[1]-Add matrices')
    print('[2]-Multiply matrix by a constant')
    print('[3]-Multiply matrices')
    print('[4]-Transpose matrix')
    print('[5]-Calculate a determinant')
    print('[6]-Inverse matrix')
    print('[0]-Exit')


# The main menu with which the program is launched
while True:
    menu()
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print('Wrong input. Enter a number!')
        continue

    if user_choice == 1:
        addition_of_two_matrices()
    elif user_choice == 2:
        multiply_by_constant()
    elif user_choice == 3:
        multiply_matrices()
    elif user_choice == 4:
        transpose_matrix()
    elif user_choice == 5:
        show_determinant()
    elif user_choice == 6:
        inverse_matrix()
    elif user_choice == 0:
        sys.exit("Goodbye!")
    else:
        print("Invalid Choice!")
