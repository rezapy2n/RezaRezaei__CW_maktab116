from fractions import Fraction

class RationalNumber:
    def __init__(self,number,number2):
        if number2 == 0:
            raise ValueError
        self.number = number
        self.number2 = number2
        self.value = Fraction(self.number,self.number2)

    def __sub__(self,other):
        return self.value - other.value

    def __add__(self,other):
        return self.value + other.value

    def __mul__(self,other):
        return self.value * other.value

    def __truediv__(self,other):
        return self.value / other.value
    

n1 = RationalNumber(10,5)
n2 = RationalNumber(17,3)

print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
