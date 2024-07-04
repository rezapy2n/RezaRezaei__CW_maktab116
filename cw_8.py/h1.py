import numpy as np

class Matrix:
    def __init__(self, data) -> None:
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape

    def __add__(self, other):
        result = self.data + other.data
        return Matrix(result)
    
    def __sub__(self, other):
        result = self.data - other.data
        return Matrix(result)
    
    def __mul__(self,other):
        result = np.dot(self.data,other.data)
        return Matrix(result)

    def __str__(self):
        return str(self.data)

A = Matrix([[1, 2], [4, 5]])
B = Matrix([[1, 2], [3, 4]])
print(A * B)