# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

# Атрибуты класса:

# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.

# Методы класса:

# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols,
#  а также создает двумерный список data размером rows x cols и заполняет его нулями.

# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами, 
# а строки разделены символами новой строки. Например:


# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, 
# которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.

# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, 
# если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.

# __add__(self, other): Метод, определяющий операцию сложения двух матриц. 

# Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов).
#  Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.

# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет,
#  что количество столбцов в первой матрице равно количеству строк во второй матрице. 
#  Если условие выполняется, создает новую матрицу, 
#  где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.

class Matrix:
    """The function performs addition and multiplication of matrices, and also outputs a string representation.
        The function performs a matrix comparison before performing operations"""

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = []
        for i in range(rows):
            self.in_data = []
            self.data.append(self.in_data)
            for y in range(cols):
                self.in_data.append(0)

    def __str__(self) -> str:
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])
    
    def __repr__(self) -> str:
        return f"Matrix({self.rows}, {self.cols})\n{matrix1.data =}\nMatrix({self.rows}, {self.cols})\n{matrix2.data = }"

    def __eq__(self, other: object) -> bool:
        return self.data == other.data

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            rows_1 = ' '.join(str(self.data[0][row] + other.data[0][row]) for row in range(self.rows+1))
            rows_2 = ' '.join(str(self.data[1][row] + other.data[1][row]) for row in range(self.rows+1))
            return f"{rows_1}\n{rows_2}"


    def __mul__(self, other):
        result = Matrix(self.rows, other.cols)
        if self.cols == other.rows:
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
                        
        return result

matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)
# Сравниваем матрицы
print(matrix1 == matrix2)
# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)
# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
