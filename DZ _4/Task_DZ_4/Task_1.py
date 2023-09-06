# ✔ Напишите функцию для транспонирования матрицы
import random 


def create_matrix(a: int, b: int, c: int, d: int) -> list:

    """The function creates and transposes a matrix. The arguments for the function are entered by the user"""

    matrix = []
    matrix_2 = []
    
    for i in range(a):
        list_in = []
        matrix.append(list_in)     
          
               

        for j in range(b):
            list_in.append(random.randint(c, d))
    print(*matrix, sep='\n')    #print() For clarity of the function

    for i in range(b):
        list_in_2 = []
        matrix_2.append(list_in_2)  
          
               

        for j in range(a):
            list_in_2.append(matrix[j][i])
    print(*matrix_2, sep='\n')    #print() For clarity of the function

    return matrix, matrix_2


l = int(input('Enter the length of the matrix: '))    
s = int(input('Enter the width of the matrix: '))
min_ = int(input('Enter the minimum value of the matrix: '))
max_ = int(input('Enter the maximum value of the matrix: '))
    
create_matrix(l, s, min_, max_)
# create_matrix(5, 2, 1, 10)




    


















# import random
# import numpy as np


# a = np.full((3, 2), random.randint(1, 10))
# b = np.array( [(1,2,3), (4,5,6), (7,8,9)] )

# print(b) 

